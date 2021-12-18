import pandas as pd
import os

# Read all files in a given directory
files = [file for file in os.listdir("Sales_Data")]
# for file in files:
#     print(file)

# ----------------------
# Create a single file reading all files in a directory
all_data = pd.DataFrame()
for file in files:
    df = pd.read_csv("Sales_Data/" + file)
    all_data = pd.concat([all_data, df])

# print(all_months_data)
all_data.to_csv("all_data_in_a_file.csv", index=False)
# all_data.head()

# ----------------------
# Do some clean-up operation in "Order Date"

# Remove all rows that contains 'NaN'.
nan_df = all_data[all_data.isna().any(axis=1)]
print(nan_df.head())

# Drop all rows containing NaN
all_data = all_data.dropna(how='any')
# all_data = all_data.dropna(how='all')
print(all_data.count())

# Some rows in "Order Data" contains string "Or". Remove those rows
all_data = all_data[all_data["Order Date"].str[0:2] != "Or"]
# print(all_data.head())

# Add a new column (Month)
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype("int32")
# print(all_data.head())

