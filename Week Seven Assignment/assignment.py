import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Explore data
print("First 5 rows:")
print(df.head())
print("\nData types and missing values:")
print(df.info())
print(df.isnull().sum())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Group by species
print("\nMean values grouped by species:")
print(df.groupby("species").mean())

# Plotting
sns.set(style="whitegrid")

# 1. Line chart (index as time)
plt.figure(figsize=(8, 4))
for species in df["species"].unique():
    subset = df[df["species"] == species]
    plt.plot(subset.index, subset["sepal length (cm)"], label=species)
plt.title("Sepal Length over Sample Index by Species")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart
plt.figure(figsize=(6, 4))
mean_petal = df.groupby("species")["petal length (cm)"].mean()
mean_petal.plot(kind="bar", color="skyblue")
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.show()

# 3. Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df["sepal width (cm)"], bins=15, kde=True)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.show()

# 4. Scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
