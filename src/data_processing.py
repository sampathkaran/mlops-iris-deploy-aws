import pandas as pd

def load_iris(data_path):
    df = pd.read_csv(data_path)
    return df