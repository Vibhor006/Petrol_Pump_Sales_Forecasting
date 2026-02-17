from src.data_pipeline import load_and_prepare_data
from src.simulation import generate_sales_and_profit
from src.insights import generate_business_insights
from src.forecasting import forecast_profit
from src.database import load_data_to_db, run_query   # ✅ NEW

# 1️⃣ Load Data
df = load_and_prepare_data("data/weekly_fuel_prices_030225.csv")
print("\nData Loaded & Cleaned Successfully")

# 2️⃣ Generate Sales & Profit
df = generate_sales_and_profit(df)
print("Sales & Profit Generated")

# 3️⃣ Load Data into SQLite Database
load_data_to_db(df)
print("Data successfully loaded into SQLite database.")

# 4️⃣ SQL KPI Analysis
print("\nSQL KPI Analysis:")

# Total Revenue
total_revenue = run_query("""
SELECT SUM(Total_Revenue) AS Total_Revenue
FROM sales_data;
""")
print("\nTotal Revenue:")
print(total_revenue)

# Average Profit
avg_profit = run_query("""
SELECT AVG(Profit) AS Average_Profit
FROM sales_data;
""")
print("\nAverage Profit:")
print(avg_profit)

# Monthly Revenue
monthly_revenue = run_query("""
SELECT strftime('%Y-%m', Date) AS Month,
       SUM(Total_Revenue) AS Monthly_Revenue
FROM sales_data
GROUP BY Month
ORDER BY Month;
""")
print("\nMonthly Revenue:")
print(monthly_revenue.head())

# 5️⃣ AI Insights
print("\nAI Business Insights:")
insights = generate_business_insights(df)
for insight in insights:
    print("-", insight)

# 6️⃣ Forecasting
forecast_df = forecast_profit(df, weeks=12)
print("\n12-Week Profit Forecast:")
print(forecast_df.head())

print("\nProject Execution Completed Successfully 🚀")
