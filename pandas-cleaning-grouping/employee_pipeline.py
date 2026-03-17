import pandas as pd
import numpy as np

# Initialize the script with the provided sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha", 
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", 
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000, 
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract", 
        "Pending docs", "Verified", 
        "Intern", "New joiner", 
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("--- Initial DataFrame ---")
print(df)
print("\n")

# 1. Detect and print the count of missing values in the dataset.
missing_values_count = df.isnull().sum()
print("--- 1. Missing Values Count ---")
print(missing_values_count)
print("\n")

# 2. Fill the missing values in the 'Salary' column using the mean of that column.
salary_mean = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(salary_mean)
print("--- 2. DataFrame after filling missing 'Salary' values ---")
print(df)
print("\n")

# 3. Drop the 'Temporary_Notes' column entirely.
df = df.drop(columns=['Temporary_Notes'])
print("--- 3. DataFrame after dropping 'Temporary_Notes' column ---")
print(df)
print("\n")

# 4. Rename the 'Salary' column to 'Annual_Salary'.
df = df.rename(columns={'Salary': 'Annual_Salary'})
print("--- 4. DataFrame after renaming 'Salary' to 'Annual_Salary' ---")
print(df)
print("\n")

# 5. Group the data by 'Department' and compute two things:
#    - The Mean salary for each department
#    - The Count of employees in each department
summary_df = df.groupby('Department').agg(
    Mean_Annual_Salary=('Annual_Salary', 'mean'),
    Employee_Count=('Employee', 'count')
).reset_index()

# 6. Print the final aggregated summary table.
print("--- Final Aggregated Summary Table ---")
print(summary_df)
