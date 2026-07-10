import pickle
from sklearn.datasets import load_diabetes

with open("diabetes_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

diabetes = load_diabetes()

new_patient = [diabetes.data[0]]

prediction = loaded_model.predict(new_patient)

print("Predicted Disease Progression:")
print(prediction)

print("\nPrediction completed without retraining.")