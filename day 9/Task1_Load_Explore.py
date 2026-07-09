import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target names
df["Species"] = [iris.target_names[i] for i in iris.target]

print("Complete Dataset")
print(df.to_string())

print("\nRows where Sepal Length > 5.0")
print(df[df["sepal length (cm)"] > 5.0])

print("\nSepal Length and Petal Length")
print(df[["sepal length (cm)", "petal length (cm)"]])

print("\nMissing Values")
print(df.isnull().sum())

print("\nSummary Statistics")
print(df.describe())

print("\nData Types")
print(df.dtypes)

# Save CSV
df.to_csv("iris_dataset.csv", index=False)

print("\nDataset saved as iris_dataset.csv")