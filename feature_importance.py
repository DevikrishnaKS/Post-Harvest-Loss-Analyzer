import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")

# Load trained model
model = joblib.load(
    "data/src/models/post_harvest_loss_model.pkl"
)

# Features used by the model
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

# Get feature importance
importance = model.feature_importances_

# Create DataFrame
importance_data = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

# Sort by importance
importance_data = importance_data.sort_values(
    by="Importance",
    ascending=False
)

print("\n===== FEATURE IMPORTANCE =====")
print(importance_data)

# Create graph
plt.figure(figsize=(10, 6))

plt.bar(
    importance_data["Feature"],
    importance_data["Importance"]
)

plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance in Post-Harvest Loss Prediction")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()