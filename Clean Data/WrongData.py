import pandas as pd

# Notes: Wrong Data in Duration column
# Example issue: a value like 450 minutes in a workout dataset is likely wrong.
# Common fixes:
# 1) Replace a specific wrong value.
# 2) Apply a boundary rule (e.g., cap Duration at 120).
# 3) Remove rows with illegal values.

df = pd.read_csv("data.csv")

print("Original DataFrame:\n")
print(df.to_string())

# 1) Replace value in one row (row index 7 in this demo).
replace_one_df = df.copy()
replace_one_df.loc[7, "Duration"] = 45

print("\n1) After setting Duration = 45 at row 7:\n")
print(replace_one_df.to_string())

# 2) Replace wrong values using a rule: if Duration > 120, set it to 120.
rule_replace_df = df.copy()
for x in rule_replace_df.index:
    if rule_replace_df.loc[x, "Duration"] > 120:
        rule_replace_df.loc[x, "Duration"] = 120

print("\n2) After capping Duration values above 120:\n")
print(rule_replace_df.to_string())

# 3) Remove rows where Duration > 120.
remove_rows_df = df.copy()
for x in remove_rows_df.index:
    if remove_rows_df.loc[x, "Duration"] > 120:
        remove_rows_df.drop(x, inplace=True)

print("\n3) After removing rows where Duration > 120:\n")
print(remove_rows_df.to_string())
