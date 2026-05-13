import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Dataset
titanic = pd.read_csv('Titanic-Dataset.csv')

# Display First 5 Rows
print("First 5 Rows:")
print(titanic.head())

# Boxplot
sns.boxplot(x='sex', y='age', hue='survived', data=titanic)
plt.title("Age Distribution by Gender and Survival")
plt.show()  

#optional
sns.violinplot(x='sex',y='age',data=titanic, hue= 'survived')
sns.catplot(x="sex", hue="survived", data=titanic, kind="count")