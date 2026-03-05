import pandas as pd

def preprocess(data):

    data = data.dropna()

    data["amount"] = data["amount"].astype(float)

    return data