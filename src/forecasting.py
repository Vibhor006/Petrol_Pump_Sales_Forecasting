import pandas as pd

def forecast_profit(df, weeks=12):
    """
    Basic forecasting (can upgrade later)
    Returns linear projection or model results.
    """
    forecast_df = df[['Date', 'Profit']].copy()
    forecast_df = forecast_df.set_index('Date')

    forecast_df = forecast_df.tail(weeks)  # placeholder

    return forecast_df
