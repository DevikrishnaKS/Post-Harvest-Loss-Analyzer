import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    try:
        data = pd.read_csv("prediction_history.csv")

        if data.empty:
            messagebox.showinfo(
                "No Data",
                "Please make at least one prediction first."
            )
            return None

        return data

    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "prediction_history.csv not found.\n"
            "Please make a prediction using GUI first."
        )
        return None


def show_analysis():

    data = load_data()

    if data is None:
        return

    total = len(data)

    average_loss = data[
        "Predicted_Loss_Percentage"
    ].mean()

    highest_loss = data[
        "Predicted_Loss_Percentage"
    ].max()

    lowest_loss = data[
        "Predicted_Loss_Percentage"
    ].min()

    low = (
        data["Loss_Level"] == "Low Loss"
    ).sum()

    medium = (
        data["Loss_Level"] == "Medium Loss"
    ).sum()

    high = (
        data["Loss_Level"] == "High Loss"
    ).sum()

    result = (
        "===== PROJECT ANALYSIS =====\n\n"
        f"Total Predictions : {total}\n\n"
        f"Average Loss      : {average_loss:.2f}%\n\n"
        f"Highest Loss      : {highest_loss:.2f}%\n\n"
        f"Lowest Loss       : {lowest_loss:.2f}%\n\n"
        "Loss Categories\n"
        "-------------------------\n"
        f"Low Loss          : {low}\n"
        f"Medium Loss       : {medium}\n"
        f"High Loss         : {high}"
    )

    result_label.config(text=result)


def show_graph():

    data = load_data()

    if data is None:
        return

    plt.figure(figsize=(9, 5))

    plt.bar(
        data["Crop"],
        data["Predicted_Loss_Percentage"]
    )

    plt.xlabel("Crop")
    plt.ylabel("Predicted Loss (%)")

    plt.title(
        "Crop-wise Post-Harvest Loss"
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


def show_category_graph():

    data = load_data()

    if data is None:
        return

    categories = [
        "Low Loss",
        "Medium Loss",
        "High Loss"
    ]

    counts = [
        (data["Loss_Level"] == "Low Loss").sum(),
        (data["Loss_Level"] == "Medium Loss").sum(),
        (data["Loss_Level"] == "High Loss").sum()
    ]

    plt.figure(figsize=(7, 5))

    plt.bar(
        categories,
        counts
    )

    plt.xlabel("Loss Category")
    plt.ylabel("Number of Predictions")

    plt.title(
        "Post-Harvest Loss Category Analysis"
    )

    plt.tight_layout()

    plt.show()


# Main window
window = tk.Tk()

window.title(
    "Post-Harvest Loss Dashboard"
)

window.geometry("550x650")


title = tk.Label(
    window,
    text="POST-HARVEST LOSS DASHBOARD",
    font=("Arial", 18, "bold")
)

title.pack(pady=25)


analysis_button = tk.Button(
    window,
    text="VIEW ANALYSIS",
    command=show_analysis,
    font=("Arial", 12, "bold"),
    width=25
)

analysis_button.pack(pady=10)


crop_graph_button = tk.Button(
    window,
    text="VIEW CROP-WISE GRAPH",
    command=show_graph,
    font=("Arial", 12, "bold"),
    width=25
)

crop_graph_button.pack(pady=10)


category_graph_button = tk.Button(
    window,
    text="VIEW LOSS CATEGORY GRAPH",
    command=show_category_graph,
    font=("Arial", 12, "bold"),
    width=25
)

category_graph_button.pack(pady=10)


result_label = tk.Label(
    window,
    text="Click VIEW ANALYSIS",
    font=("Arial", 12),
    justify="left"
)

result_label.pack(pady=30)


window.mainloop()