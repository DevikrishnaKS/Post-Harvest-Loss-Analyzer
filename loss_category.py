import pandas as pd

# Load prediction results
data = pd.read_csv("prediction_results.csv")

# Function to classify loss
def classify_loss(loss):
    if loss < 10:
        return "Low Loss"
    elif loss < 20:
        return "Medium Loss"
    else:
        return "High Loss"

# Apply classification
data["Loss_Level"] = data["Predicted_Loss_Percentage"].apply(classify_loss)

# Display result
print(data[
    [
        "Crop",
        "Predicted_Loss_Percentage",
        "Loss_Level"
    ]
])

# Save final results
data.to_csv("final_analysis.csv", index=False)

print("\nFinal analysis saved successfully")