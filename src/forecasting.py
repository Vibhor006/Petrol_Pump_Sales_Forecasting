from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def forecast_profit(df, weeks=12):
    df = df.copy()
    df = df.sort_values('Date')
    
    df['Time_Index'] = np.arange(len(df))
    
    X = df[['Time_Index']]
    y = df['Profit']
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_index = np.arange(len(df), len(df) + weeks)
    future_profit = model.predict(future_index.reshape(-1, 1))
    
    future_dates = pd.date_range(
        start=df['Date'].max(),
        periods=weeks+1,
        freq='W'
    )[1:]
    
    forecast_df = pd.DataFrame({
        'Date': future_dates,
        'Predicted_Profit': future_profit
    })
    
    return forecast_df
