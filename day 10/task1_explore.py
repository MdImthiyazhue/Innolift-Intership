import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris(as_frame=True)

df = iris.frame

# Rename target column
df["Species"] = df["target"].map(dict(enumerate(iris.target_names)))
df.drop(columns=["target"], inplace=True)

print("First 5 Rows")
print(df.head())

print("\nFlower Count in Each Species")
print(df["Species"].value_counts())

print("\nAverage Features for Each Species")
print(df.groupby("Species").mean())

dataset_avg = df["petal length (cm)"].mean()

print("\nVirginica Flowers with Petal Length > Dataset Average")
filtered = df[
    (df["Species"] == "virginica") &
    (df["petal length (cm)"] > dataset_avg)
]

print(filtered)

highest_species = (
    df.groupby("Species")["sepal length (cm)"]
    .mean()
    .idxmax()
)

print("\nSpecies with Highest Average Sepal Length:")
print(highest_species)

df["Sepal Area"] = (
    df["sepal length (cm)"] *
    df["sepal width (cm)"]
)

df.to_csv("filtered_iris.csv", index=False)

print("\nfiltered_iris.csv saved successfully.")