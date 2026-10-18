import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
import pandas as pd

# Read CSV file
df = pd.read_csv('data.csv')

# Print first and last rows
print(df)

# Print entire DataFrame
print(df.to_string())

# Check maximum display rows
print(pd.options.display.max_rows)

# Change maximum display rows
pd.options.display.max_rows = 9999

# Print again after increasing limit
print(df)