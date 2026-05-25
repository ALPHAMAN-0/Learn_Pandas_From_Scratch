import pandas as pd

# Note: Handling cells with wrong date format in the "Date" column.
df = pd.read_csv("data.csv")

print("Original DataFrame:\n")
print(df.to_string())

# Convert all values in "Date" to datetime.
# Wrong/missing values become NaT (Not a Time).
df["Date"] = pd.to_datetime(df["Date"], format="mixed", errors="coerce")

print("\nAfter converting Date to datetime:\n")
print(df.to_string())

# Remove rows where Date is NaT (null datetime).
df.dropna(subset=["Date"], inplace=True)

print("\nAfter removing rows with NULL/NaT in Date:\n")
print(df.to_string())
