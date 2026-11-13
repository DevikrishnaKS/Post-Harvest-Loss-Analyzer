import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error


# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")


# Features
features = [
    "Harvested_Quantity",
    "Marketable_Quantity",
    "Temperature",
    "Humidity",
    "Storage_Days",
    "Transportation_Hours",
    "Pest_Level",
    "Damage_Level"
]


# Calculate actual loss percentage
data["Loss_Quantity"] = (
    data["Harvested_Quantity"]
    - data["Marketable_Quantity"]
)

data["Loss_Percentage"] = (
    data["Loss_Quantity"]
    / data["Harvested_Quantity"]
) * 100


X = data[features]
y = data["Loss_Percentage"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}


print("\n===== MODEL COMPARISON =====\n")


for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    print(name)
    print("MAE :", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("---------------------------")


print("\nModel comparison completed successfully.")