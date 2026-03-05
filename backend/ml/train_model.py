import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Get project root path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

data_path = os.path.join(BASE_DIR, "data", "transactions.csv")

print("Loading dataset from:", data_path)

data = pd.read_csv(data_path)

X = data.drop("fraud", axis=1)
y = data["fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = RandomForestClassifier(n_estimators=100)

model.fit(X_train, y_train)

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

joblib.dump(model, model_path)

print("Model trained and saved:", model_path)