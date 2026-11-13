import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")

# Load trained model
model = joblib.load(
    "data/src/models/post_harvest_loss_model.pkl"
)

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

data["Actual_Loss_Percentage"] = (
    data["Loss_Quantity"]
    / data["Harvested_Quantity"]
) * 100

# Predict using ML model
data["Predicted_Loss_Percentage"] = model.predict(
    data[features]
)

# Display results
print("\n===== ACTUAL VS PREDICTED =====")

print(
    data[
        [
            "Crop",
            "Actual_Loss_Percentage",
            "Predicted_Loss_Percentage"
        ]
    ]
)

# Create graph
plt.figure(figsize=(10, 6))

x = range(len(data))

plt.plot(
    x,
    data["Actual_Loss_Percentage"],
    marker="o",
    label="Actual Loss"
)

plt.plot(
    x,
    data["Predicted_Loss_Percentage"],
    marker="o",
    label="Predicted Loss"
)

plt.xticks(
    x,
    data["Crop"],
    rotation=45
)

plt.xlabel("Crop")
plt.ylabel("Loss Percentage (%)")
plt.title("Actual vs Predicted Post-Harvest Loss")

plt.legend()
plt.tight_layout()

plt.show()