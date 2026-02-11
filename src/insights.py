def generate_business_insights(df):
    insights = []
    
    if df['Profit'].mean() > 0:
        insights.append("Business is profitable on average.")
    else:
        insights.append("Business is running at a loss.")
    
    corr = df['Petrol_Price'].corr(df['Petrol_Sales_Liters'])
    
    if corr < -0.5:
        insights.append("High price sensitivity detected in petrol sales.")
    
    if df['Profit'].iloc[-1] > df['Profit'].mean():
        insights.append("Recent performance is above average.")
    
    return insights
