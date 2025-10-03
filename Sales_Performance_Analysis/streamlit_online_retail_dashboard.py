# ===========================================
# Online Retail II Analytics - Streamlit Executive Dashboard (Pandas Only)
# ===========================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import streamlit as st
import plotly.express as px
import base64
import os
import zipfile

# -------------------------------------------
# Dataset Auto-Detection & Extraction
# -------------------------------------------
csv_filename = "online_retail_II.csv"
zip_path = "online_retail.zip"

def get_dataset_path():
    # Case 1: CSV already extracted
    if os.path.exists(csv_filename):
        return csv_filename

    # Case 2: ZIP exists, extract CSV
    elif os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall()
            for f in z.namelist():
                if f.endswith(".csv"):
                    return f

    # Case 3: Nothing found
    else:
        st.error("❌ Dataset not found. Please upload `online_retail.zip` or `online_retail_II.csv`.")
        st.stop()

dataset_path = get_dataset_path()


# -------------------------------------------
# Background Image Setup
# -------------------------------------------
st.set_page_config(page_title="Online Retail II Dashboard", layout="wide")

@st.cache_data
def get_img_as_base64(file_path: str) -> str | None:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

background_path = r"backg.jpg"  # <-- replace with your path
backgr = get_img_as_base64(background_path)
if backgr:
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{backgr}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"] {{
        background: rgba(0,0,0,0.5);
    }}
    </style>
    """, unsafe_allow_html=True)


# -------------------------------------------
# 1. Data Preparation (Pandas Version)
# -------------------------------------------
@st.cache_data
def prep_dataset():
    data = pd.read_csv(dataset_path)
    data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
    data = data.drop_duplicates()

    # Fill missing descriptions with canonical description
    desc_counts = (
        data[data['description'].notna()]
        .groupby(['stockcode', 'description'])
        .size()
        .reset_index(name='count')
    )
    desc_counts['rank'] = desc_counts.groupby('stockcode')['count'] \
                                    .rank(method='dense', ascending=False)

    canonical_desc = {}
    for stockcode, group in desc_counts.groupby('stockcode'):
        top_rank = group[group['rank'] == 1].sort_values('description')
        idx = len(top_rank) // 2
        canonical_desc[stockcode] = top_rank.iloc[idx]['description']

    data['description'] = data.apply(
        lambda row: canonical_desc.get(row['stockcode'], row['description'])
        if pd.isna(row['description']) or row['description']=='' else row['description'],
        axis=1
    )
    data = data.dropna(subset=['description'])
    return data


# -------------------------------------------
# 2. Feature Engineering
# -------------------------------------------
def feature_engineering(data):
    data['IsCancellation'] = data['invoice'].astype(str).str.startswith('C')
    data['IsReturn'] = data['quantity'] < 0
    data['Revenue'] = data['quantity'] * data['price']
    data['customer_id'] = data['customer_id'].astype(str).replace('nan', 'Guest')
    data['customer_type'] = data['customer_id'].apply(lambda x: 'Guest' if x=='Guest' else 'Registered')
    data['IsGiveaway'] = (data['Revenue'] <= 0)
    data['LostRevenue'] = np.where(data['IsCancellation'] | data['IsReturn'], data['Revenue'], 0)
    data['invoicedate'] = pd.to_datetime(data['invoicedate'])
    return data


# -------------------------------------------
# 3. Customer Segmentation
# -------------------------------------------
def customer_segments(data):
    df = data[data['customer_id'] != 'Guest'].copy()
    customer_features = (
        df.groupby('customer_id')
        .agg(
            total_invoices=('invoice', 'count'),
            canceled_invoices=('IsCancellation', 'sum'),
            return_invoices=('IsReturn', 'sum'),
            total_revenue=('Revenue', 'sum')
        )
        .reset_index()
    )
    customer_features['cancellation_rate'] = customer_features['canceled_invoices'] / customer_features['total_invoices']
    customer_features['avg_invoice_value'] = customer_features['total_revenue'] / customer_features['total_invoices']

    features = ['cancellation_rate', 'total_invoices', 'avg_invoice_value']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(customer_features[features])

    kmeans = KMeans(n_clusters=4, random_state=42)
    customer_features['cluster'] = kmeans.fit_predict(X_scaled)

    cluster_order = customer_features.groupby('cluster')['cancellation_rate'].mean().sort_values(ascending=False).index
    segment_names = ["Unreliable One-Timers", "Casual Buyers", "Steady Spenders", "Loyal High-Value Customers"]
    mapping = {c: segment_names[i] for i, c in enumerate(cluster_order)}
    customer_features['risk_segment'] = customer_features['cluster'].map(mapping)
    return customer_features


# -------------------------------------------
# 4. Product Analytics
# -------------------------------------------
def product_analytics(data):
    df_prod = data.copy()
    df_prod.columns = df_prod.columns.str.strip()

    product_summary = (
        df_prod.groupby(["stockcode", "description"], as_index=False)
        .agg(
            total_transactions=("invoice", "count"),
            cancellations=("IsCancellation", "sum"),
            returns=("IsReturn", "sum"),
            giveaways=("IsGiveaway", "sum"),
            revenue=("Revenue", "sum")
        )
    )

    product_summary["cancellation_rate"] = product_summary["cancellations"] / product_summary["total_transactions"]
    product_summary["return_rate"] = product_summary["returns"] / product_summary["total_transactions"]
    product_summary["giveaway_rate"] = product_summary["giveaways"] / product_summary["total_transactions"]
    mean_price = df_prod['price'].mean()
    product_summary["lost_revenue"] = (
        (product_summary["cancellations"] + product_summary["returns"]) * mean_price
    )

    return product_summary


# -------------------------------------------
# 5. Load and preprocess data
# -------------------------------------------
data = prep_dataset()
data = feature_engineering(data)
customer_features = customer_segments(data)
product_summary = product_analytics(data)

# -------------------------------------------
# 6. Streamlit Tabs & Visuals (Unchanged)
# -------------------------------------------
tab1, tab2, tab3 = st.tabs(["Executive Overview", "Customer Analytics", "Product Analytics"])

# -- Tab 1: Executive Overview
with tab1:
    st.header("🔹 Executive Overview")
    total_rev = data['Revenue'].sum()
    lost_rev = data['LostRevenue'].sum()
    net_rev = total_rev - lost_rev
    cancel_rate = data['IsCancellation'].mean()*100

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("💰 Total Revenue", f"${total_rev:,.0f}")
    kpi2.metric("📉 Lost Revenue", f"${lost_rev:,.0f}")
    kpi3.metric("📈 Net Revenue", f"${net_rev:,.0f}")
    kpi4.metric("❌ Cancellation Rate", f"{cancel_rate:.2f}%")

    # Revenue & Cancellation charts
    col1, col2 = st.columns(2)
    with col1:
        rev_summary = data.groupby('customer_type').agg(
            Revenue=('Revenue', lambda x: x.sum() - data.loc[x.index,'LostRevenue'].sum()),
            LostRevenue=('LostRevenue','sum')
        ).reset_index()
        fig_rev = px.bar(
            rev_summary,
            x='customer_type',
            y=['Revenue','LostRevenue'],
            barmode='group',
            text_auto='.2s',
            template='plotly_dark',
            color_discrete_map={'Revenue':'#00FFAA','LostRevenue':'#FF5555'},
            title="Revenue vs Lost Revenue by Customer Type",
            width=600, height=400
        )
        st.plotly_chart(fig_rev)

    with col2:
        cancel_summary = data.groupby('customer_type')['IsCancellation'].mean().reset_index()
        cancel_summary['CancellationPct'] = cancel_summary['IsCancellation']*100
        fig_cancel = px.bar(
            cancel_summary,
            x='customer_type',
            y='CancellationPct',
            text=cancel_summary['CancellationPct'].apply(lambda x: f"{x:.2f}%"),
            color='CancellationPct',
            template='plotly_dark',
            color_continuous_scale='Reds',
            title="Cancellation Rate (%) by Customer Type",
            width=600, height=400
        )
        fig_cancel.update_traces(textposition='outside')
        st.plotly_chart(fig_cancel)

    # Revenue Share by Country
    country_rev = (
        data.groupby('country')
        .agg(Revenue=('Revenue', lambda x: x.sum() - data.loc[x.index,'LostRevenue'].sum()))
        .sort_values('Revenue', ascending=False)
        .reset_index()
    )
    top_countries = country_rev.head(5)
    other_rev = pd.DataFrame({'country': ['Other'], 'Revenue': [country_rev['Revenue'][5:].sum()]})
    country_rev_final = pd.concat([top_countries, other_rev], ignore_index=True).sort_values('Revenue', ascending=True)
    fig_country = px.bar(
        country_rev_final,
        x='Revenue',
        y='country',
        orientation='h',
        text='Revenue',
        color='Revenue',
        template='plotly_dark',
        color_continuous_scale='Greens',
        title="Revenue Share by Country (Top 5 + Other)",
        width=1200, height=500
    )
    fig_country.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
    st.plotly_chart(fig_country)

# -- Tab 2 & 3 remain unchanged (Customer & Product Analytics)
# Copy your previous code for tabs 2 and 3 here
