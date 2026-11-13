import pandas as pd
import joblib

# Load model
model = joblib.load(
    "data/src/models/post_harvest_loss_model.pkl"
)

print("\n===== SMART POST-HARVEST RECOMMENDATION =====\n")

# User inputs
crop = input("Enter Crop Name: ")

harvested = float(input("Enter Harvested Quantity: "))
marketable = float(input("Enter Marketable Quantity: "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
storage_days = float(input("Enter Storage Days: "))
transportation = float(input("Enter Transportation Hours: "))
pest = float(input("Enter Pest Level: "))
damage = float(input("Enter Damage Level: "))

# Prepare input
input_data = pd.DataFrame([[
    harvested,
    marketable,
    temperature,
    humidity,
    storage_days,
    transportation,
    pest,
    damage
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

# Prediction
prediction = model.predict(input_data)[0]

# Loss category
if prediction < 10:
    level = "Low Loss"
elif prediction < 20:
    level = "Medium Loss"
else:
    level = "High Loss"

# Recommendations
if level == "Low Loss":

    recommendation = (
        "Maintain the current storage and transportation practices. "
        "Continue regular monitoring."
    )

elif level == "Medium Loss":

    recommendation = (
        "Improve storage conditions, reduce unnecessary storage time, "
        "and monitor transportation conditions."
    )

else:

    recommendation = (
        "Immediate corrective action is recommended. "
        "Check storage conditions, pest damage, physical damage, "
        "and transportation practices."
    )

# Display result
print("\n===== ANALYSIS RESULT =====")

print("Crop:", crop)
print("Predicted Loss:", round(prediction, 2), "%")
print("Loss Level:", level)

print("\nRecommendation:")
print(recommendation)

print("\nAnalysis completed successfully.")