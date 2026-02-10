import pandas as pd

# Load processed dataset
df = pd.read_csv("../data/petrol_business_dataset.csv")

print("\n=== Petrol Pump Price Simulation Tool ===")

average_profit = df['Profit'].mean()

while True:
    try:
        print("\nEnter new price scenario (or type 'exit' to stop)")

        petrol_input = input("Enter expected Petrol Price: ")
        if petrol_input.lower() == "exit":
            break

        diesel_input = input("Enter expected Diesel Price: ")
        if diesel_input.lower() == "exit":
            break

        new_petrol_price = float(petrol_input)
        new_diesel_price = float(diesel_input)

        # Demand model
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
        print(f"Estimated Profit: ₹{predicted_profit:,.2f}")

        if predicted_profit > average_profit:
            print("📈 This pricing strategy may increase profitability.")
        else:
            print("📉 This pricing strategy may reduce profitability.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
