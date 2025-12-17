import pandas as pd

df = pd.read_csv("outputs/cleaned_data.csv")

# Create Age Groups
df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[18, 25, 35, 45, 60],
    labels=['18-25', '26-35', '36-45', '46-60']
)

# Create Salary Slabs
df['SalarySlab'] = pd.cut(
    df['MonthlyIncome'],
    bins=[0, 3000, 6000, 10000, 20000],
    labels=['Low', 'Medium', 'High', 'Very High']
)

# Save file for Tableau
df.to_csv("outputs/tableau_hr_attrition.csv", index=False)

print("Tableau dataset exported successfully.")
