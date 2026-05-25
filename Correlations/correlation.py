import pandas as pd

# Finding Relationships (Child-Friendly Notes)
# ------------------------------------------------------------
# Think of correlation like this:
# "When one thing moves, does the other thing move too?"
#
# corr() gives numbers from -1 to 1.
# 1.0  -> perfect team: they go up together.
# 0.9  -> very strong team.
# 0.0  -> no clear team.
# -0.9 -> strong opposite team: if one goes up, the other goes down.
#
# A simple rule:
# Good correlation is usually >= 0.6 or <= -0.6.
#
# Also important:
# corr() only works with numeric columns.
# Text columns like Date are ignored.


def label_strength(value: float) -> str:
	"""Return a simple child-friendly label for correlation strength."""
	abs_value = abs(value)
	if abs_value == 1:
		return "perfect"
	if abs_value >= 0.6:
		return "good"
	if abs_value >= 0.3:
		return "okay"
	return "weak"


def explain_pair(matrix: pd.DataFrame, left: str, right: str) -> None:
	"""Print a short easy explanation for one pair of columns."""
	value = matrix.loc[left, right]
	strength = label_strength(value)
	direction = "same direction" if value >= 0 else "opposite direction"
	print(f"- {left} vs {right}: {value:.6f} -> {strength} ({direction})")


try:
	# If you place a data.csv near this file, it will use your real data.
	df = pd.read_csv("data.csv")
except FileNotFoundError:
	# Fallback demo data so this lesson always runs.
	df = pd.DataFrame(
		{
			"Duration": [60, 60, 45, 30, 90, 120],
			"Pulse": [110, 117, 109, 98, 105, 108],
			"Maxpulse": [130, 145, 175, 124, 132, 140],
			"Calories": [409.1, 479.0, 282.4, 269.0, 350.0, 500.0],
			"Date": [
				"2020/12/01",
				"2020/12/02",
				"2020/12/03",
				"2020/12/04",
				"2020/12/05",
				"2020/12/06",
			],
		}
	)

print("Data preview:\n")
print(df.head().to_string(index=False))

print("\nCorrelation table (only numeric columns):\n")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix.to_string())

print("\nSimple explanation:")
if {"Duration", "Calories"}.issubset(corr_matrix.columns):
	explain_pair(corr_matrix, "Duration", "Calories")

if {"Duration", "Maxpulse"}.issubset(corr_matrix.columns):
	explain_pair(corr_matrix, "Duration", "Maxpulse")

print("\nRemember:")
print("- Each column with itself is always 1.0 (perfect).")
print("- Numbers near 0 mean weak relationship.")
print("- Numbers near 1 or -1 mean strong relationship.")
