import subprocess
import sys


def run_file(file):
    print("\n==========================================")
    print("Running:", file)
    print("==========================================\n")

    result = subprocess.run([sys.executable, file])

    if result.returncode != 0:
        print("\nERROR while running:", file)
    else:
        print("\nCompleted:", file)


def run_all():
    files = [
        "data/src/data_loading.py",
        "data/src/data_cleaning.py",
        "data/src/loss_calculation.py",
        "data/src/graphs.py",
        "data/src/model_training.py",
        "data/src/prediction.py",
        "data/src/loss_category.py",
        "data/src/model_evaluation.py",
        "data/src/feature_importance.py",
        "data/src/actual_vs_predicted.py",
        "data/src/model_comparison.py",
    ]

    for file in files:
        run_file(file)

    print("\n==========================================")
    print("       ALL ANALYSIS COMPLETED")
    print("==========================================\n")


while True:

    print("\n")
    print("==========================================")
    print("       POST-HARVEST LOSS ANALYZER")
    print("==========================================")

    print("\n1. Data Loading")
    print("2. Data Cleaning")
    print("3. Loss Calculation")
    print("4. Graphs")
    print("5. Model Training")
    print("6. Prediction")
    print("7. Loss Category")
    print("8. Model Evaluation")
    print("9. Feature Importance")
    print("10. Actual vs Predicted")
    print("11. Model Comparison")
    print("12. Open GUI")
    print("13. Open Dashboard")
    print("14. Run Complete Project")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        run_file("data/src/data_loading.py")

    elif choice == "2":
        run_file("data/src/data_cleaning.py")

    elif choice == "3":
        run_file("data/src/loss_calculation.py")

    elif choice == "4":
        run_file("data/src/graphs.py")

    elif choice == "5":
        run_file("data/src/model_training.py")

    elif choice == "6":
        run_file("data/src/prediction.py")

    elif choice == "7":
        run_file("data/src/loss_category.py")

    elif choice == "8":
        run_file("data/src/model_evaluation.py")

    elif choice == "9":
        run_file("data/src/feature_importance.py")

    elif choice == "10":
        run_file("data/src/actual_vs_predicted.py")

    elif choice == "11":
        run_file("data/src/model_comparison.py")

    elif choice == "12":
        print("\nOpening Post-Harvest Loss Analyzer GUI...\n")
        subprocess.run([sys.executable, "gui.py"])

    elif choice == "13":
        print("\nOpening Dashboard...\n")
        subprocess.run([sys.executable, "dashboard.py"])

    elif choice == "14":
        run_all()

        print("\nOpening GUI...")
        subprocess.run([sys.executable, "gui.py"])

    elif choice == "0":
        print("\nThank you for using Post-Harvest Loss Analyzer!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 0 to 14.")

        