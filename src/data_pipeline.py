import pandas as pd
import numpy as np


def load_and_prepare_data(file_path):
    """
    Loads raw fuel price dataset and performs cleaning.
    Returns cleaned dataframe.
    """

    # -------------------------------
    # 1. Load Dataset
    # -------------------------------
    df = pd.read_csv(file_path)

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

    df['Petrol_Sales_Liters'] = (
        15000 - (df['Petrol_Price'] * 20)
        + np.random.normal(0, 500, len(df))
    )

    df['Diesel_Sales_Liters'] = (
        12000 - (df['Diesel_Price'] * 15)
        + np.random.normal(0, 400, len(df))
    )

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

    return df
