#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

#Two  lines to make our compiler able to draw:
# Save to a file instead of writing raw image bytes to the terminal stdout
plt.savefig("plot.png")
print("Saved plot.png")
