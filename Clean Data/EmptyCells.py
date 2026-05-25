import pandas as pd

df = pd.read_csv('data.csv')

print("Original DataFrame:\n")
print(df.to_string())

print("\nDataFrame after dropna():\n")
new_df = df.dropna()

print(new_df.to_string())

print("\nFill missing Calories with 130:\n")
fill_130_df = df.copy()
fill_130_df.fillna({"Calories": 130}, inplace=True)

print(fill_130_df.to_string())

print("\nFill missing Calories with mean:\n")
mean_df = df.copy()
x = mean_df["Calories"].mean()
mean_df.fillna({"Calories": x}, inplace=True)

print(mean_df.to_string())

print("\nFill missing Calories with median:\n")
median_df = df.copy()
x = median_df["Calories"].median()
median_df.fillna({"Calories": x}, inplace=True)

print(median_df.to_string())

print("\nFill missing Calories with mode:\n")
mode_df = df.copy()
x = mode_df["Calories"].mode()[0]
mode_df.fillna({"Calories": x}, inplace=True)

print(mode_df.to_string())
