☕ Café Sales Data Analysis
📌 Business Value Proposition

This project transforms raw café sales data into actionable insights, helping management understand sales patterns, optimize revenue, and make data-driven decisions. By cleaning inconsistencies, exploring revenue drivers, and visualizing performance trends, the analysis enables the café to:

Optimize pricing and promotions.

Improve inventory management.

Identify cross-selling opportunities.

Implement targeted loyalty programs.

🛠 Tools & Libraries

Python

Pandas & DuckDB (data cleaning, querying)

Seaborn & Matplotlib (visualizations)

📊 Data Overview
Column Name	Meaning
transaction_id	Unique ID of each transaction
item	Product sold (Coffee, Cookie, Tea, etc.)
quantity	Number of units sold
price_per_unit	Price per unit
total_spent	Quantity × Price per unit
payment_method	Cash, Credit Card, Digital Wallet, or Undefined
location	Store branch/location
transaction_date	Date of transaction
🧹 Data Cleaning and Preprocessing
Missing Value Summary
Column	Missing (%)	Cleaning Strategy
transaction_date	4.6%	Filled missing dates with the median date to preserve temporal continuity
item	9.7%	Imputed missing items using the menu table based on price_per_unit
quantity	4.8%	Imputed using total_spent / price_per_unit
price_per_unit	5.3%	Imputed using total_spent / quantity
total_spent	5.0%	Imputed using quantity × price_per_unit
payment_method	31.8%	Replaced errors/missing values with 'Undefined'
location	39.6%	Replaced errors/missing values with 'Undefined'
Visualization of Missing Values
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_cleaning_summary = pd.DataFrame({
    "Column": ["transaction_date", "item", "quantity", "price_per_unit", "total_spent", "payment_method", "location"],
    "Missing_Percent": [4.6, 9.7, 4.8, 5.3, 5.0, 31.8, 39.6]
})

plt.figure(figsize=(10,6))
sns.barplot(
    x="Column",
    y="Missing_Percent",
    data=data_cleaning_summary,
    palette="Set2"
)
plt.title("🧹 Data Cleaning: Percentage of Missing Values by Column", fontsize=16)
plt.ylabel("Missing Values (%)")
plt.xlabel("Column")
plt.xticks(rotation=30)
plt.ylim(0, 45)
plt.tight_layout()
plt.show()


Key Takeaways:

location and payment_method have the highest missing rates, limiting branch-level or payment-based insights.

Low-to-moderate missing values in item, quantity, price_per_unit, and total_spent were imputed to maintain analytical continuity.

Visualization communicates data quality clearly before moving to revenue and performance analysis.

🔑 Business Questions & Insights
1️⃣ Which category drives more revenue: Drinks or Snacks?

Approach: Grouped items into Snacks (Cookie, Salad, Cake, Sandwich) and Drinks (Coffee, Tea, Smoothie, Juice). Aggregated revenue and sales volume.

Insight: Snacks generate higher revenue overall, though volumes are similar. Top performers: Juice and Salad. Lowest performers: Tea and Cookies.

Actionable: Consider bundling high-volume, low-revenue items with bestsellers to improve revenue.

2️⃣ Are high-selling items profitable?

Insight: Quantity alone does not explain revenue differences — some items sell in high volumes but contribute less revenue.

Actionable: Use this to design bundles or promotions targeting items that underperform in revenue but sell frequently.

3️⃣ What are the busiest days?

Approach: Classified days as Weekday (Mon–Fri) vs Weekend (Sat–Sun) using transaction_date. Aggregated revenue and transaction counts. Excluded rows with imputed dates (~4.6%).

Insight: Weekdays and weekends show distinguishable patterns in sales volume.

Actionable: Optimize staffing, stock, and promotions according to peak periods.

4️⃣ How do payment methods impact sales?

Approach: Aggregated revenue and transaction counts by payment_method, including “Undefined” for missing/erroneous data.

Insight: Cash, Credit Card, and Digital Wallet perform almost identically. “Undefined” is the largest category, highlighting data capture issues.

Actionable:

Implement loyalty programs and promotions for popular payment methods.

Fix data capture to uncover trends for targeted campaigns.

5️⃣ What cross-selling opportunities exist?

Insight: Without customer IDs, segmentation is limited.

Actionable: Introduce customer tracking to enable cross-selling (e.g., pairing drinks with snacks: 2 Tea + 3 Cookies).

6️⃣ Time-based performance

Insight: Daily line plots are noisy; aggregation or rolling averages recommended.

Actionable: Focus on aggregated trends for operational and promotional decision-making.

📈 Visualizations

Revenue vs Items (bar plots)

Quantity Sold vs Items (bar plots)

Revenue by Category (Snacks vs Drinks)

Revenue & Transactions by Day Type (Weekday vs Weekend)

Payment Method Impact (bar plots including “Undefined”)

Data Cleaning Missing Percentages (bar plot above)

🚀 Suggested Strategies

Price Optimization: Adjust prices for high-volume, low-revenue items.

Bundling & Promotions: Bundle high-performing items with underperforming ones.

Operational Efficiency: Allocate staffing and stock based on trends.

Customer Tracking & Loyalty Programs: Enable cross-selling opportunities.

Improve Data Capture: Reduce “Undefined” entries to improve insights.

🔮 Expanded Next Steps / Further Analysis

Customer Segmentation

Background: Without customer IDs, it’s difficult to understand purchasing behavior and frequency.

Data-Driven Opportunity: By implementing unique customer tracking (loyalty cards, email-based accounts, or digital payments), we can segment customers by spending patterns, purchase frequency, and product preferences.

Expected Impact: Enables personalized promotions, identifies high-value customers, and provides cross-selling opportunities.

Time-Series Forecasting for Demand Prediction

Background: Daily sales trends show variability, and weekend/weekday effects are observable but noisy due to missing/imputed transaction dates.

Data-Driven Opportunity: Aggregating sales at a weekly or hourly level and applying forecasting models (e.g., ARIMA, Prophet) can predict demand for each item.

Expected Impact: Optimizes inventory management, reduces stock-outs, and ensures sufficient preparation for high-demand periods.

Market Basket Analysis for Cross-Selling

Background: Café items often complement each other (e.g., drinks and snacks). Current dataset lacks customer-level identification.

Data-Driven Opportunity: With customer tracking, we can analyze which items are frequently purchased together and create bundles or promotional combinations.

Expected Impact: Increases average transaction value, improves revenue from underperforming items, and enhances customer experience.

Interactive Dashboard Implementation

Background: Static reports provide insights but are limited in accessibility and interactivity.

Data-Driven Opportunity: Using tools like Streamlit or Power BI, we can create dashboards showing revenue by item, category, day type, and payment method.

Expected Impact: Enables real-time monitoring, supports operational decisions, and provides an easily interpretable interface for management.

Improving Data Quality & Collection Processes

Background: High percentages of missing values in payment_method (31.8%) and location (39.6%) limit analysis.

Data-Driven Opportunity: Standardizing data entry, enforcing mandatory fields, or integrating digital payment tracking can reduce errors.

Expected Impact: More accurate revenue, transaction, and trend analysis, enabling branch-level insights and reliable segmentation.

🏁 Conclusion

This analysis provides a fundamental understanding of café performance, highlighting revenue drivers, operational trends, and opportunities for revenue optimization. By combining cleaned data, category analysis, and payment insights, it enables actionable strategies for promotions, inventory management, and cross-selling.