import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("outputs/cleaned_data.csv")

# Attrition count
sns.countplot(x='Attrition', data=df)
plt.title("Attrition Count")
plt.savefig("outputs/plots/attrition_count.png")
plt.show()

# Attrition by Department
sns.countplot(x='Department', hue='Attrition', data=df)
plt.title("Attrition by Department")
plt.xticks(rotation=45)
plt.savefig("outputs/plots/attrition_by_department.png")
plt.show()

# Attrition vs Monthly Income
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title("Attrition vs Monthly Income")
plt.savefig("outputs/plots/attrition_income.png")
plt.show()
