import pandas as pd
import joblib

# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")

# Load trained model
model = joblib.load("data/src/models/post_harvest_loss_model.pkl")

# Use the same features used during training
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

# Make prediction
predictions = model.predict(X)

# Add prediction
data["Predicted_Loss_Percentage"] = predictions

# Display result
print(data[
    [
        "Crop",
        "Harvested_Quantity",
        "Marketable_Quantity",
        "Predicted_Loss_Percentage"
    ]
])
# Save prediction results
data.to_csv("prediction_results.csv", index=False)

print("Prediction results saved successfully")