import pickle

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Values")
print(y_test)

print("\nPredicted Values")
print(predictions)

mse = mean_squared_error(y_test, predictions)

print("\nMean Squared Error:", mse)

with open("diabetes_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved as diabetes_model.pkl")