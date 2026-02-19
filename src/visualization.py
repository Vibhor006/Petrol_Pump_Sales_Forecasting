import matplotlib.pyplot as plt


def plot_revenue_trend(df):
    """
    Plot Total Revenue over time
    """
    plt.figure()
    plt.plot(df['Date'], df['Total_Revenue'])
    plt.title("Total Revenue Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_profit_trend(df):
    """
    Plot Profit over time
    """
    plt.figure()
    plt.plot(df['Date'], df['Profit'])
    plt.title("Profit Over Time")
    plt.xlabel("Date")
    plt.ylabel("Profit")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_sales_comparison(df):
    """
    Compare Petrol vs Diesel sales
    """
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


def plot_price_vs_sales(df):
    """
    Scatter plot: Price vs Sales
    """
    plt.figure()
    plt.scatter(df['Petrol_Price'], df['Petrol_Sales_Liters'])
    plt.title("Petrol Price vs Petrol Sales")
    plt.xlabel("Petrol Price")
    plt.ylabel("Petrol Sales")
    plt.tight_layout()
    plt.show()
