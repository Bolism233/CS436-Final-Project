import pandas as pd

# Load the dataset
df = pd.read_csv("ILINet.csv")

# Combine "YEAR" and "WEEK" to create a "date" column for every row
df['date'] = pd.to_datetime(df['YEAR'].astype(str) + df['WEEK'].astype(str) + '0', format='%Y%U%w')

# Format the date to "YYYY-MM-DD 00:00:00"
df['date'] = df['date'].dt.strftime('%Y-%m-%d 00:00:00')

# Reorder columns to make 'date' the first column
cols = ['date'] + [col for col in df.columns if col != 'date']
df = df[cols]

# Optionally, drop the original YEAR and WEEK columns if you no longer need them
df.drop(columns=['YEAR', 'WEEK'], inplace=True)

# Display the result
print(df.head())

# Save the transformed DataFrame to a new CSV file
df.to_csv("transformed_ILINet.csv", index=False)
