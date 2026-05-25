import pandas as pd

# Notes: Discovering and removing duplicate rows.
# Duplicate rows are rows that appear more than one time.
# Use duplicated() to discover duplicates and drop_duplicates() to remove them.

df = pd.read_csv("data.csv")

print("Original DataFrame:\n")
print(df.to_string())

# Make sure there is at least one duplicate row for demo output.
if not df.duplicated().any():
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
    print("\nNo duplicates found in source file, so one demo duplicate row was added.\n")
    print(df.to_string())

print("\nDuplicate check (True means duplicate row):\n")
print(df.duplicated())

# Remove duplicate rows.
clean_df = df.copy()
clean_df.drop_duplicates(inplace=True)

print("\nAfter drop_duplicates():\n")
print(clean_df.to_string())
