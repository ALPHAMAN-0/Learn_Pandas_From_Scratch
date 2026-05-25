import pandas as pd
import matplotlib.pyplot as plt

# Simple plotting demo for `data.csv` in the same folder.
# Plots:
#  - Scatter: Duration vs Calories
#  - Line: Duration over Date (if Date exists)

try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    raise SystemExit("data.csv not found in the same folder. Put your CSV next to this script.")

# Normalize Date if present
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Basic scatter: Duration vs Calories
plt.figure(figsize=(8, 5))
if {"Duration", "Calories"}.issubset(df.columns):
    plt.scatter(df["Duration"], df["Calories"], color="tab:blue", alpha=0.8)
    plt.title("Duration vs Calories")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Calories")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("plot_duration_vs_calories.png")
    print("Saved plot_duration_vs_calories.png")
    try:
        plt.show()
    except Exception:
        pass
else:
    print("Duration and/or Calories column not found; skipping scatter.")

# If Date exists, show Duration over time
if "Date" in df.columns and df["Date"].notna().any():
    df_sorted = df.dropna(subset=["Date"]).sort_values("Date")
    if "Duration" in df_sorted.columns:
        plt.figure(figsize=(10, 4))
        plt.plot(df_sorted["Date"], df_sorted["Duration"], marker="o", linestyle="-", color="tab:green")
        plt.title("Duration over Time")
        plt.xlabel("Date")
        plt.ylabel("Duration (minutes)")
        plt.xticks(rotation=45)
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig("plot_duration_over_time.png")
        print("Saved plot_duration_over_time.png")
        try:
            plt.show()
        except Exception:
            pass

print("Done.")
