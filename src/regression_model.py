
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb

def load_data(filepath):
    """Load and return cleaned healthcare breach data."""
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    return df

def preprocess_data(df):
    """Encode categorical variables and prepare features/target."""
    X = pd.get_dummies(df[['State', 'Covered Entity Type', 'Type of Breach', 'Year']], drop_first=True)
    y = np.log1p(df['Individuals Affected'])  # log1p handles log(0) cases
    return X, y

def train_model(X, y):
    """Train XGBRegressor and return model with evaluation metrics."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = {
        "MSE": mean_squared_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "MAE": mean_absolute_error(y_test, y_pred),
        "R2": r2_score(y_test, y_pred)
    }
    return model, metrics

def print_metrics(metrics):
    print("Model performance:")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    # Modify the path as needed
    data_path = "healthcare_breaches.csv"
    df = load_data(data_path)
    X, y = preprocess_data(df)
    model, metrics = train_model(X, y)
    print_metrics(metrics)
