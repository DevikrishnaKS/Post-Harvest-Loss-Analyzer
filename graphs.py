import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")

# Calculate loss
data["Loss_Quantity"] = (
    data["Harvested_Quantity"] -
    data["Marketable_Quantity"]
)

data["Loss_Percentage"] = (
    data["Loss_Quantity"] /
    data["Harvested_Quantity"]
) * 100


# Graph 1: Crop vs Loss Percentage
plt.figure(figsize=(8, 5))

plt.bar(
    data["Crop"],
    data["Loss_Percentage"]
)

plt.xlabel("Crop")
plt.ylabel("Loss Percentage (%)")
plt.title("Crop-wise Post-Harvest Loss")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Graph 2: Temperature vs Loss
plt.figure(figsize=(8, 5))

plt.scatter(
    data["Temperature"],
    data["Loss_Percentage"]
)

plt.xlabel("Temperature")
plt.ylabel("Loss Percentage (%)")
plt.title("Temperature vs Post-Harvest Loss")

plt.tight_layout()
plt.show()


# Graph 3: Storage Days vs Loss
plt.figure(figsize=(8, 5))

plt.scatter(
    data["Storage_Days"],
    data["Loss_Percentage"]
)

plt.xlabel("Storage Days")
plt.ylabel("Loss Percentage (%)")
plt.title("Storage Days vs Post-Harvest Loss")

plt.tight_layout()
plt.show()