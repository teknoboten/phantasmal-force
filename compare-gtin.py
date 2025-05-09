import pandas as pd

output_csv_path = 'output.csv'
currentcat_csv_path = 'currentcat.csv'

# Read the CSV files into DataFrames, ensuring GTIN is read as a string
output_df = pd.read_csv(output_csv_path, dtype={'GTIN': 'str', 'SKU': 'str'})
currentcat_df = pd.read_csv(currentcat_csv_path, dtype={'GTIN': 'str', 6: 'str', 7: 'str', 8: 'str', 23: 'str', 24: 'str', 25: 'str'})

# Extract GTIN columns as sets for comparison, stripping any leading/trailing whitespaces
output_gtin_set = set(output_df['GTIN'].str.strip())
currentcat_gtin_set = set(currentcat_df['GTIN'].str.strip())

# Find GTINs that are in output_df but not in currentcat_df
new_gtins = output_gtin_set - currentcat_gtin_set

# Debugging output
# print('New GTINs:', new_gtins)

# Filter the new items based on the new GTINs
new_items_df = output_df[output_df['GTIN'].str.strip().isin(new_gtins)]

# Output the new items to a new CSV file
new_items_df.to_csv('new_items.csv', index=False)

# Display the DataFrame of new items to verify
print(new_items_df)
print('Success! You compared the things!')
print('new items:', len(new_items_df))