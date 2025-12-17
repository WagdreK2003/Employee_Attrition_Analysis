import pandas as pd

# Load dataset
df = pd.read_csv("data/HR_Employee_Attrition.csv")

# Check basic info
print(df.info())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert Attrition to numeric
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Remove unnecessary columns
columns_to_drop = ['EmployeeCount', 'Over18', 'StandardHours']
df.drop(columns=columns_to_drop, inplace=True)

# Save cleaned data
df.to_csv("outputs/cleaned_data.csv", index=False)

print("Data cleaning completed successfully.")
