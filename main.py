import joblib
import pandas as pd

# Load trained model
model = joblib.load(
    "data/src/models/post_harvest_loss_model.pkl"
)

print("\n===== POST-HARVEST LOSS ANALYZER =====\n")

# User inputs
harvested = float(input("Enter Harvested Quantity: "))
marketable = float(input("Enter Marketable Quantity: "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
storage_days = float(input("Enter Storage Days: "))
transportation_hours = float(input("Enter Transportation Hours: "))
pest_level = float(input("Enter Pest Level: "))
damage_level = float(input("Enter Damage Level: "))

# Create input data
input_data = pd.DataFrame([[
    harvested,
    marketable,
    temperature,
    humidity,
    storage_days,
    transportation_hours,
    pest_level,
    damage_level
]], columns=[
    "Harvested_Quantity",
    "Marketable_Quantity",
    "Temperature",
    "Humidity",
    "Storage_Days",
    "Transportation_Hours",
    "Pest_Level",
    "Damage_Level"
])

# Predict
prediction = model.predict(input_data)[0]

# Loss classification
if prediction < 10:
    loss_level = "Low Loss"
elif prediction < 20:
    loss_level = "Medium Loss"
else:
    loss_level = "High Loss"

# Display result
print("\n===== PREDICTION RESULT =====")
print("Predicted Loss Percentage:", round(prediction, 2), "%")
print("Loss Level:", loss_level)