import pandas as pd

# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")

# Calculate loss quantity
data["Loss_Quantity"] = (
    data["Harvested_Quantity"] - data["Marketable_Quantity"]
)

# Calculate loss percentage
data["Loss_Percentage"] = (
    data["Loss_Quantity"] / data["Harvested_Quantity"]
) * 100

# Display result
print(data[
    [
        "Crop",
        "Harvested_Quantity",
        "Marketable_Quantity",
        "Loss_Quantity",
        "Loss_Percentage"
    ]
])