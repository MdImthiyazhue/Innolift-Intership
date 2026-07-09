from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Values")
print(y_test)

print("\nPredicted Values")
print(predictions)

print("\nComparison")

for actual, predicted in zip(y_test, predictions):
    print(f"Actual: {iris.target_names[actual]}  |  Predicted: {iris.target_names[predicted]}")