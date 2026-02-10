import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("../data/weekly_fuel_prices_030225.csv")


# -------------------------------
# 2. Convert Date & Sort
# -------------------------------
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.sort_values('Date')

# -------------------------------
# 3. Handle Missing Values
# -------------------------------
df = df.ffill()

# -------------------------------
# 4. Clean Column Names
# -------------------------------
df.columns = (
    df.columns
    .str.replace(":", "", regex=False)
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("%", "percent", regex=False)
    .str.replace("/", "_", regex=False)
    .str.replace(" ", "_", regex=False)
)

# -------------------------------
# 5. Rename Important Columns
# -------------------------------
df = df.rename(columns={
    '_ULSP__Pump_price_p_litre': 'Petrol_Price',
    'ULSD_Pump_price_p_litre': 'Diesel_Price'
})

# -------------------------------
# 6. Generate Synthetic Sales
# -------------------------------
np.random.seed(42)

df['Petrol_Sales_Liters'] = 15000 - (df['Petrol_Price'] * 20) + np.random.normal(0, 500, len(df))
df['Diesel_Sales_Liters'] = 12000 - (df['Diesel_Price'] * 15) + np.random.normal(0, 400, len(df))

df['Petrol_Sales_Liters'] = df['Petrol_Sales_Liters'].clip(lower=5000)
df['Diesel_Sales_Liters'] = df['Diesel_Sales_Liters'].clip(lower=4000)

# -------------------------------
# 7. Revenue Calculation
# -------------------------------
df['Petrol_Revenue'] = df['Petrol_Sales_Liters'] * df['Petrol_Price']
df['Diesel_Revenue'] = df['Diesel_Sales_Liters'] * df['Diesel_Price']
df['Total_Revenue'] = df['Petrol_Revenue'] + df['Diesel_Revenue']

# -------------------------------
# 8. Operating Cost & Profit
# -------------------------------
df['Operating_Cost'] = 300000 + (df['Total_Revenue'] * 0.05)
df['Profit'] = df['Total_Revenue'] - df['Operating_Cost']

print("\nSample Revenue & Profit:")
print(df[['Date', 'Total_Revenue', 'Profit']].head())

# -------------------------------
# 9. Visualizations
# -------------------------------

plt.figure()
plt.plot(df['Date'], df['Total_Revenue'])
plt.title("Total Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df['Date'], df['Profit'])
plt.title("Profit Over Time")
plt.xlabel("Date")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df['Date'], df['Petrol_Sales_Liters'], label='Petrol')
plt.plot(df['Date'], df['Diesel_Sales_Liters'], label='Diesel')
plt.title("Petrol vs Diesel Sales")
plt.xlabel("Date")
plt.ylabel("Sales (Liters)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df['Petrol_Price'], df['Petrol_Sales_Liters'])
plt.title("Petrol Price vs Petrol Sales")
plt.xlabel("Petrol Price")
plt.ylabel("Petrol Sales")
plt.tight_layout()
plt.show()

print("\nCorrelation Matrix:")
print(df[['Petrol_Price','Petrol_Sales_Liters',
          'Diesel_Price','Diesel_Sales_Liters']].corr())

# -------------------------------
# 10. Export Final Dataset
# -------------------------------
df.to_csv("../data/petrol_business_dataset.csv", index=False)

print("\nFinal dataset saved as petrol_business_dataset.csv")
print("Saved in:", os.getcwd())

# -------------------------------
# 11. Interactive Price Simulation
# -------------------------------

print("\n--- Petrol Pump Price Simulation Tool ---")

try:
    new_petrol_price = float(input("Enter expected Petrol Price: "))
    new_diesel_price = float(input("Enter expected Diesel Price: "))

    # Predict sales using demand model
    predicted_petrol_sales = 15000 - (new_petrol_price * 20)
    predicted_diesel_sales = 12000 - (new_diesel_price * 15)

    predicted_petrol_sales = max(predicted_petrol_sales, 5000)
    predicted_diesel_sales = max(predicted_diesel_sales, 4000)

    # Revenue
    predicted_petrol_revenue = predicted_petrol_sales * new_petrol_price
    predicted_diesel_revenue = predicted_diesel_sales * new_diesel_price
    predicted_total_revenue = predicted_petrol_revenue + predicted_diesel_revenue

    # Cost & Profit
    predicted_operating_cost = 300000 + (predicted_total_revenue * 0.05)
    predicted_profit = predicted_total_revenue - predicted_operating_cost

    print("\n--- Simulation Result ---")
    print(f"Predicted Petrol Sales: {predicted_petrol_sales:.2f} liters")
    print(f"Predicted Diesel Sales: {predicted_diesel_sales:.2f} liters")
    print(f"Estimated Total Revenue: ₹{predicted_total_revenue:,.2f}")
    print(f"Estimated Profit: ₹{predicted_profit:,.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values only.")
