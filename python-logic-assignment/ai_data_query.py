import pandas as pd

# 1. Sample Dataset: Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Score": [92.5, 78.0, 88.5, 95.0, 65.0, 89.0],
    "Passed": [True, False, True, True, False, True],
    "Category": ["A", "B", "A", "A", "C", "B"]
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print()

# 2. Operations to Perform

# Single Column: Select the Name column and print it.
print("--- Single Column: Name ---")
name_column = df['Name']
print(name_column)
print()

# Multiple Columns: Select the Name and Score columns, store them in a new DataFrame, and print it.
print("--- Multiple Columns: Name and Score ---")
name_score_df = df[['Name', 'Score']]
print(name_score_df)
print()

# iloc: Use iloc to retrieve the first three rows and print them.
print("--- iloc: First Three Rows ---")
first_three_rows = df.iloc[:3]
print(first_three_rows)
print()

# loc: Set the Name column as a meaningful index on a copy of the DataFrame, 
# then use loc to retrieve a specific row by name and print it.
print("--- loc: Specific Row by Name ---")
df_copy = df.copy()
df_copy.set_index('Name', inplace=True)
charlie_row = df_copy.loc['Charlie']
print(charlie_row)
print()

# Basic Filter: Filter rows where Score > 85 and print the result.
print("--- Basic Filter: Score > 85 ---")
high_score_filter = df[df['Score'] > 85]
print(high_score_filter)
print()

# Multiple Condition Filter: Filter rows where Score > 85 AND Passed == True.
# Using the & operator and proper parentheses for grouping.
print("--- Multiple Condition Filter: Score > 85 AND Passed == True ---")
multiple_condition_filter = df[(df['Score'] > 85) & (df['Passed'] == True)]
print(multiple_condition_filter)
print()

# Chaining & Sorting: Chain a filtering and sorting operation together.
# Filter for Score > 85 and Passed == True, then sort descending by Score.
print("--- High-performing students: ---")
high_performing_students = (
    df[(df['Score'] > 85) & (df['Passed'] == True)]
    .sort_values(by='Score', ascending=False)
)
print(high_performing_students)
