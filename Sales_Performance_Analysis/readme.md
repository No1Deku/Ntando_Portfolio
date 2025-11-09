🛒 Online Retail II — Executive Insights & Analytics Dashboard
Data-Driven Risk Detection, Customer Segmentation, and Revenue Intelligence

This project transforms a messy, real-world retail dataset into an executive-grade decision system.
It combines EDA, behavioral segmentation, anomaly detection, and an interactive Streamlit dashboard to surface insights on cancellations, fraud patterns, product risk, and high-value customer behavior.

Designed for executives, strategy teams, and business leaders, not only data practitioners.

📂 Repository Structure
📁 online-retail-analytics
│── README.md
│── retail_dashboard.py           # Streamlit executive dashboard
│── data_preparation.ipynb        # EDA + cleaning + feature engineering
│── clustering_rfm.ipynb          # Segmentation workflow
│── model_outputs/                # Scaled features, clusters, exports
│── /assets                       # All dashboard visuals and charts
│── Online Retail II.csv          # Dataset

🗂️ 1. Project Objective
What this project solves and why it matters

The objective is to build a retail sales-performance intelligence system that answers high-level business questions:

Why is revenue being lost through cancellations and returns?

Which customers represent long-term value or risk?

Which products create dissatisfaction or contribute to ROI leakage?

Where do suspicious or anomalous transactions occur?

How should executives prioritize retention, quality control, and market expansion?

This dashboard equips decision-makers with clear, actionable metrics, not raw data tables.

🛠️ 2. Data Understanding
What’s in the dataset and why it matters

The dataset includes:

Category	Fields	Purpose
Invoices	InvoiceNo, InvoiceDate	Detect cancellations, fraud, seasonality
Products	StockCode, Description, Price, Quantity	Product performance, return rates, giveaways
Customers	CustomerID, Country	Loyalty identification and geographic risk
Transactions	Line totals, timestamps	Revenue, lost revenue, order patterns
Key Data Challenges

These challenges reflect real retail problems:

Missing product descriptions

Negative or zero quantity (returns, giveaways, fraudulent adjustments)

Missing CustomerID (guest shoppers)

UK-heavy distribution dominating the dataset

Duplicate SKUs with inconsistent descriptions

Each issue was reframed as business intelligence, not “noise.”

🧹 3. Data Cleaning & Feature Engineering
Turning chaotic data into business-ready signals
✅ Flags engineered to expose risk patterns:
Feature	Meaning
IsCancellation	Invoices starting with "C"
IsReturn	Negative quantity
IsGiveaway	Price ≤ 0 or Qty ≤ 0
IsGuestCustomer	Missing CustomerID
LostRevenue	Revenue lost through cancellations/returns
✅ Other cleaning operations:

Standardized column names

Removed duplicates

Used DuckDB SQL to map StockCode → most frequent Description

Filtered but preserved negative transactions for revenue-risk analysis

Parsed InvoiceDate for seasonality and trend analysis

Business Value:
These steps exposed operational inefficiencies, product risks, and revenue leakage.

📊 4. Exploratory Data Checks (EDA)

EDA focused on quality diagnostics relevant to executive decisions:

✅ Missing Data

Description and CustomerID were the most incomplete fields

Guest transactions often correlated with higher return/cancellation risk

✅ Time Validity

Checked the full invoice date range to ensure no corrupted timestamps.

✅ Geographic Distribution

Over 85 percent of transactions occurred in the UK

Non-UK countries were normalized or grouped for stable insights

✅ Product-Level Analysis

Calculated SKU-level return rates

Identified items with high lost-revenue ratios

Flagged products with extreme cancellation patterns

✅ Customer Behavior

Frequency and monetary value distribution

Guest vs registered behavior differences

✅ Anomaly Detection

Flagged suspicious spikes in cancellations or bulk returns.

🎯 5. Executive-Level Business Questions

This project answers questions executives care about—not just technical metrics.

Area	Question	Strategic Value
Cancellations & Giveaways	What is the financial impact?	Cut losses, spot fraud
	Which products/customers create high cancellation rates?	Improve product strategy
Customer Behavior	Do guest customers behave differently?	Strengthen loyalty strategy
Country Insights	Are non-UK regions growing?	Identify new markets
Product Strategy	Which SKUs cause the most returns?	Improve supplier decisions
🧠 6. Customer Segmentation (RFM + K-Means)
✅ RFM Metrics

Recency: Days since last purchase

Frequency: Total invoices

Monetary: Total revenue

✅ Workflow

Remove cancellations and giveaways

Aggregate RFM per customer

Scale numerical features

Determine k using Elbow Method

Cluster using K-Means

Interpret segments meaningfully

✅ Customer Segments Identified
Segment	Description
🚩 Unreliable One-Timers	High cancellations, low value
🛍️ Casual Buyers	Irregular purchases, moderate risk
💳 Steady Spenders	Consistent, predictable revenue
👑 Loyal High-Value Customers	Reliable, high lifetime value
Enhancements

Added CancellationRate, GiveawayCount, IsGuest

Performed segment comparison by country and SKU category

Business Value:
Segmentation supports targeted retention and product personalization.

📈 7. Dashboard Design
Structured for executive decision-making
Section	Visuals	Insights
Sales Overview	KPIs, trend lines, revenue net vs lost	Macro performance
Cancellations & Giveaways	Bar charts, KPI cards	Financial leakage, fraud indicators
Customer Segments	Cluster plots, tables	Loyalty, value, churn risk
Product Performance	Bar charts, return-rate maps	Quality and profitability
Country-Level Insights	Map visuals	Market concentration, expansion spots
Risk & Anomalies	Heatmaps, time-based spikes	Fraud & operational risks
Dashboard Filters

Time range

Country

Customer type

Product SKU

Segment

Design Guidelines

Executive-first narrative

Story starts with wins → moves to risk → ends with strategy

Avoid sparse slicing (group small countries)

📊 8. Key Insights Delivered
✅ Fraud & Cancellation Risk

Some countries show unusually high cancellation ratios, indicating possible fraud or fulfillment issues.

✅ Loyalty Gaps

Registered customers canceled more often than guests, suggesting loyalty programs may not be aligned to customer needs.

✅ Product-Level ROI Drain

A handful of SKUs produced disproportionate lost revenue through returns and giveaways.

✅ Revenue Concentration Risk

UK concentration creates vulnerability.
Diversification into secondary markets is strategically valuable.

✅ Guest vs Registered Behavior

Guest customers buy frequently but inconsistently.
Registered customers provide value but churn at higher rates.

🧭 9. Business Recommendations
1. Reduce Cancellation Leakage

Investigate high-risk countries and SKUs

Enforce review of cancellation reasons

Introduce SKU-level quality audits

2. Strengthen Customer Loyalty

Build personalized campaigns for Steady Spenders and Loyal High-Value customers

Address gaps contributing to registered-customer cancellations

3. Optimize Product Strategy

Use return/cancellation ratios to decide discontinuations

Flag low-ROI promotions with high giveaway rates

4. Market Expansion Strategy

Identify and prioritize non-UK markets with meaningful revenue contributions

5. Risk Monitoring System

Automate anomaly detection for bulk returns or suspicious invoices

🛠️ 10. Tech Stack

Python: pandas, numpy, scikit-learn, duckdb

Dashboard: Streamlit + Plotly

Clustering: K-Means, feature scaling

Data Processing: SQL with DuckDB

Visualization: Plotly, matplotlib

🧠 11. Lessons Learned

Data quality issues often reveal deeper business problems

Combining SQL + Python accelerates cleaning workflows

Behavioral segmentation provides more value than demographics

Negative quantities are not noise—often revenue-risk signals

Executive dashboards must simplify, not overwhelm
