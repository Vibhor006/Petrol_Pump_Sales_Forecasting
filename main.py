from src.data_pipeline import load_and_prepare_data
from src.simulation import generate_sales_and_profit
from src.insights import generate_business_insights
from src.forecasting import forecast_profit

# 1️⃣ Load Data
df = load_and_prepare_data("data/weekly_fuel_prices_030225.csv")
print("\nData Loaded & Cleaned Successfully")

# 2️⃣ Generate Sales & Profit
df = generate_sales_and_profit(df)
print("Sales & Profit Generated")

# 3️⃣ AI Insights
print("\nAI Business Insights:")
insights = generate_business_insights(df)

for insight in insights:
    print("-", insight)

# 4️⃣ Forecasting
forecast_df = forecast_profit(df, weeks=12)
print("\n12-Week Profit Forecast:")
print(forecast_df.head())

print("\nProject Execution Completed Successfully 🚀")
