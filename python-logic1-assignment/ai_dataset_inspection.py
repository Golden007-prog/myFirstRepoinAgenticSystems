import pandas as pd

# Generate a small sample DataFrame with at least 10 rows
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kevin'],
    'Age': [25, 30, 35, 28, 22, 40, 32, 29, 26, 38, 45],
    'Score': [85, 92, 78, 88, 95, 70, 82, 90, 85, 76, 60],
    'Label': ['Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Fail', 'Fail']
}
df_generated = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename = 'sample_dataset.csv'
df_generated.to_csv(csv_filename, index=False)

# Load it back into a new DataFrame using read_csv
df = pd.read_csv(csv_filename)

# Display the first 5 rows
print("\n--- First 5 rows ---")
print(df.head())

# Display the last 5 rows
print("\n--- Last 5 rows ---")
print(df.tail())

# Display structural information
print("\n--- Structural Information ---")
df.info()

# Display summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Select a single column and store it in a new variable
age_column = df['Age']
print("\n--- Single Column Selection ('Age') - First 5 rows ---")
print(age_column.head())

# Select multiple columns and store them in a new DataFrame
subset_df = df[['Name', 'Score']]
print("\n--- Multiple Column Selection ('Name', 'Score') - First 5 rows ---")
print(subset_df.head())

# Filter rows based on a numerical condition using Pandas vectorized operations
# (Strict constraint: No manual for loops used)
filtered_rows = df[df['Score'] > 80]

print("\n--- Filtered rows (Score > 80): ---")
print(filtered_rows)
