from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def train_models(df):
    """
    Train ML models to predict Profit.
    Returns trained models and test data.
    """

    # -------------------------------
    # Feature Selection
    # -------------------------------
    features = [
        'Petrol_Price',
        'Diesel_Price',
        'Petrol_Sales_Liters',
        'Diesel_Sales_Liters',
        'Total_Revenue'
    ]

    target = 'Profit'

    X = df[features]
    y = df[target]

    # -------------------------------
    # Train-Test Split
    # -------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------------
    # Initialize Models
    # -------------------------------
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(random_state=42)
    }

    trained_models = {}

    # -------------------------------
    # Train Models
    # -------------------------------
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model

    return trained_models, X_test, y_test
