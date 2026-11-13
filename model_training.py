import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib


# ==========================================
# LOAD DATA
# ==========================================

data = pd.read_csv(
    "data/Agriculture_data.csv"
)


# ==========================================
# CALCULATE LOSS PERCENTAGE
# ==========================================

data["Loss_Percentage"] = (
    (
        data["Harvested_Quantity"]
        - data["Marketable_Quantity"]
    )
    / data["Harvested_Quantity"]
) * 100


# ==========================================
# FEATURES
# ==========================================

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


# ==========================================
# TARGET
# ==========================================

y = data["Loss_Percentage"]


# ==========================================
# TRAIN RANDOM FOREST MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


# ==========================================
# SAVE TRAINED MODEL
# ==========================================

joblib.dump(
    model,
    "data/src/models/post_harvest_loss_model.pkl"
)


print("Model Trained Successfully")
print("Model Saved Successfully")