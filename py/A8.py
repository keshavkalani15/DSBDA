import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Titanic Dataset
titanic = pd.read_csv('Titanic-Dataset.csv')

# Display First 5 Rows
print("First 5 Rows:")
print(titanic.head())

# Dataset Information
print("\nDataset Information:")
print(titanic.info())

# Pattern Visualization using Seaborn
sns.countplot(x='survived', hue='Sex', data=titanic)
plt.title("Survival Count")
plt.show()

# Histogram for Fare Distribution
plt.hist(titanic['fare'])
plt.title("Distribution of Titanic Fare")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.show()

#optional

sns.boxplot(x='class',y='age',data=titanic)
plt.show()

sns.scatterplot(x='age',y='fare',data=titanic,hue='survived')
plt.show()

