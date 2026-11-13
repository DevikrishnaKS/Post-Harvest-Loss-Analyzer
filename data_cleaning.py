import pandas as pd

# Load dataset
data = pd.read_csv("data/Agriculture_data.csv")

# Display dataset information
print("Dataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())