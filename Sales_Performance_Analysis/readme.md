🛒 Online Retail II Analytics – Executive Dashboard
📌 Project Overview

This project transforms messy retail transaction data into executive-level business insights using advanced data analytics and interactive dashboards.
Instead of stopping at simple KPIs like “total sales,” this dashboard reveals:

Fraud and cancellation risks

ROI leakage from returns and giveaways

Customer behavior patterns via segmentation

Product-level risks and performance

Geographic revenue concentration

Built with Streamlit + Python + Plotly, it bridges exploratory data analysis (EDA) with decision-ready executive dashboards.

⚙️ Tech Stack

Python Libraries: pandas, numpy, duckdb, scikit-learn, plotly, streamlit

Techniques: Data cleaning, feature engineering, clustering, anomaly detection, segmentation, dashboarding

🔑 Analytical Workflow
1. Data Preparation

Standardized column names, removed duplicates.

Used DuckDB SQL queries to assign canonical product descriptions for missing/duplicate values.

Removed incomplete transactions but reframed anomalies as insights instead of discarding them.

Business Value:
Data cleaning exposed inefficiencies—fraudulent cancellations, untraceable guest IDs, and promotional giveaways. These anomalies were reframed as strategic risk indicators.

2. Feature Engineering

Created features aligned with business pain points:

IsCancellation, IsReturn, IsGiveaway → Transaction-level risk flags

Revenue & LostRevenue → Measured impact of fraud/returns

Customer_Type (Guest vs Registered) → Loyalty segmentation

InvoiceDate parsing → Seasonal and trend analysis

Business Value:
Feature engineering translated raw sales into actionable business KPIs, making fraud, dissatisfaction, and marketing inefficiencies measurable.

3. Customer Segmentation (K-Means Clustering)

Applied K-Means on scaled behavioral features:

Cancellation rate

Total invoices

Average invoice value

Segments Identified:

🚩 Unreliable One-Timers – high cancellations, low engagement

🛍️ Casual Buyers – irregular, low spenders

💳 Steady Spenders – consistent, mid-level value

👑 Loyal High-Value Customers – reliable revenue drivers

Business Value:
Instead of demographic buckets, segmentation was behavior-based, empowering targeted loyalty campaigns and retention strategies.

4. Product Analytics

Grouped transactions at SKU level to analyze:

Cancellation rate

Return rate

Giveaway rate

Lost revenue per product

Business Value:

Identified products with quality or expectation mismatches (high return rates).

Highlighted SKUs causing disproportionate lost revenue.

Enabled smarter promotional targeting.

5. Executive Dashboard (Streamlit)

Delivered insights via an interactive, executive-ready dashboard with three views:

Executive Overview (Macro View)

KPIs: Total Revenue, Lost Revenue, Net Revenue, Cancellation Rate

Revenue vs Lost Revenue (by customer type)

Country-level revenue distribution

Customer Analytics (Micro View)

Registered vs Guest contribution

Avg Revenue per Customer

Cancellation rates by customer risk segment

Product Analytics (Meso View)

Top 10 products by cancellations, returns, and lost revenue

Product-level ROI table with cancellation/return rates

Business Value:
Executives can drill down into:

High-risk geographies

Products driving dissatisfaction

Customer segments worth retaining

ROI performance of promotions

📊 Key Insights Delivered

Fraud Detection:

Countries with suspiciously high cancellation rates flagged for monitoring.

Customer Loyalty Risks:

Registered customers canceled more than guests, suggesting unmet loyalty expectations.

Hidden ROI Drain:

Returns and giveaways eroded revenue on select SKUs, signaling product/marketing inefficiencies.

Revenue Concentration Risk:

Overdependence on UK market → diversification needed.