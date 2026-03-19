import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("diabetes.csv")

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved")