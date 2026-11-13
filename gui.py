import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load(
    "data/src/models/post_harvest_loss_model.pkl"
)


# ==========================================
# PREDICT LOSS FUNCTION
# ==========================================

def predict_loss():

    try:

        # Get crop name
        crop = entry_crop.get()

        if crop == "":
            messagebox.showerror(
                "Error",
                "Please enter crop name."
            )
            return


        # Get input values
        harvested = float(entry_harvested.get())
        marketable = float(entry_marketable.get())
        temperature = float(entry_temperature.get())
        humidity = float(entry_humidity.get())
        storage_days = float(entry_storage.get())
        transportation = float(entry_transportation.get())
        pest = float(entry_pest.get())
        damage = float(entry_damage.get())


        # ==========================================
        # CREATE INPUT DATA
        # ==========================================

        input_data = pd.DataFrame(
            [[
                harvested,
                marketable,
                temperature,
                humidity,
                storage_days,
                transportation,
                pest,
                damage
            ]],
            columns=[
                "Harvested_Quantity",
                "Marketable_Quantity",
                "Temperature",
                "Humidity",
                "Storage_Days",
                "Transportation_Hours",
                "Pest_Level",
                "Damage_Level"
            ]
        )


        # ==========================================
        # PREDICT LOSS
        # ==========================================

        prediction = model.predict(input_data)[0]


        # ==========================================
        # CLASSIFY LOSS
        # ==========================================

        if prediction < 10:

            level = "Low Loss"

        elif prediction < 20:

            level = "Medium Loss"

        else:

            level = "High Loss"


        # ==========================================
        # RECOMMENDATION
        # ==========================================

        if level == "Low Loss":

            recommendation = (
                "Maintain the current storage and "
                "transportation practices."
            )

        elif level == "Medium Loss":

            recommendation = (
                "Improve storage conditions and reduce "
                "unnecessary storage time."
            )

        else:

            recommendation = (
                "Immediate corrective action is recommended. "
                "Check storage, pest damage and "
                "transportation conditions."
            )


        # ==========================================
        # DISPLAY RESULT
        # ==========================================

        result_label.config(
            text=
            f"Crop: {crop}\n\n"
            f"Predicted Loss: {prediction:.2f}%\n\n"
            f"Loss Level: {level}\n\n"
            f"Recommendation:\n"
            f"{recommendation}"
        )


        # ==========================================
        # SAVE PREDICTION HISTORY
        # ==========================================

        result = pd.DataFrame([{

            "Crop": crop,

            "Harvested_Quantity": harvested,

            "Marketable_Quantity": marketable,

            "Temperature": temperature,

            "Humidity": humidity,

            "Storage_Days": storage_days,

            "Transportation_Hours": transportation,

            "Pest_Level": pest,

            "Damage_Level": damage,

            "Predicted_Loss_Percentage":
                round(prediction, 2),

            "Loss_Level": level

        }])


        # Check existing history file
        try:

            old_data = pd.read_csv(
                "prediction_history.csv"
            )

            result = pd.concat(
                [old_data, result],
                ignore_index=True
            )

        except FileNotFoundError:

            pass


        # Save history
        result.to_csv(
            "prediction_history.csv",
            index=False
        )


    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )


# ==========================================
# RESET FUNCTION
# ==========================================

def reset_fields():

    entry_crop.delete(0, tk.END)

    entry_harvested.delete(0, tk.END)

    entry_marketable.delete(0, tk.END)

    entry_temperature.delete(0, tk.END)

    entry_humidity.delete(0, tk.END)

    entry_storage.delete(0, tk.END)

    entry_transportation.delete(0, tk.END)

    entry_pest.delete(0, tk.END)

    entry_damage.delete(0, tk.END)


    result_label.config(
        text="Prediction will appear here"
    )


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title(
    "Post-Harvest Loss Analyzer"
)

window.geometry(
    "550x750"
)


# ==========================================
# TITLE
# ==========================================

title = tk.Label(

    window,

    text="POST-HARVEST LOSS ANALYZER",

    font=("Arial", 18, "bold")

)

title.pack(pady=15)


# ==========================================
# INPUT CREATION FUNCTION
# ==========================================

def create_input(label_text):

    label = tk.Label(

        window,

        text=label_text,

        font=("Arial", 10)

    )

    label.pack()


    entry = tk.Entry(

        window,

        width=35

    )

    entry.pack(pady=4)


    return entry


# ==========================================
# INPUT FIELDS
# ==========================================

entry_crop = create_input(
    "Crop Name"
)

entry_harvested = create_input(
    "Harvested Quantity"
)

entry_marketable = create_input(
    "Marketable Quantity"
)

entry_temperature = create_input(
    "Temperature"
)

entry_humidity = create_input(
    "Humidity"
)

entry_storage = create_input(
    "Storage Days"
)

entry_transportation = create_input(
    "Transportation Hours"
)

entry_pest = create_input(
    "Pest Level"
)

entry_damage = create_input(
    "Damage Level"
)


# ==========================================
# PREDICT BUTTON
# ==========================================

predict_button = tk.Button(

    window,

    text="PREDICT LOSS",

    command=predict_loss,

    font=("Arial", 12, "bold"),

    width=20

)

predict_button.pack(pady=10)


# ==========================================
# RESET BUTTON
# ==========================================

reset_button = tk.Button(

    window,

    text="RESET",

    command=reset_fields,

    font=("Arial", 11),

    width=20

)

reset_button.pack(pady=5)


# ==========================================
# RESULT DISPLAY
# ==========================================

result_label = tk.Label(

    window,

    text="Prediction will appear here",

    font=("Arial", 12, "bold"),

    wraplength=480,

    justify="left"

)

result_label.pack(pady=25)


# ==========================================
# START GUI
# ==========================================

window.mainloop()