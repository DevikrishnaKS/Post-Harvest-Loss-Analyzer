import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")

# Load model
model = joblib.load(
    "data/src/models/post_harvest_loss_model.pkl"
)

# Features
X = data[
    [
        "Harvested_Quantity",
        "Marketable_Quantity",
        "Temperature",
        "Humidity",
        "Storage_Days",
        "Transportation_Hours",
        "Pest_Level",
        "Damage_Level"
    ]
]

# Actual loss percentage
data["Loss_Quantity"] = (
    data["Harvested_Quantity"] -
    data["Marketable_Quantity"]
)

data["Actual_Loss_Percentage"] = (
    data["Loss_Quantity"] /
    data["Harvested_Quantity"]
) * 100

# Prediction
predictions = model.predict(X)

# Evaluation
mae = mean_absolute_error(
    data["Actual_Loss_Percentage"],
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        data["Actual_Loss_Percentage"],
        predictions
    )
)

print("\n===== MODEL EVALUATION =====")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))

print("\nEvaluation completed successfully.")