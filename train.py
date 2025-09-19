# import pandas as pd
from pathlib import Path
import os
import sys # used to pass command line arguments
import joblib

"""
Defining the PACAKGE_ROOT to point to the right package folder.
``` sys.path ``` is where the python looks for pacakages
``` __file__ ``` is a builtin variable that stores the path of the current file
Path().parent is used to go one level up in the directory structure

"""
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# download from local pacakage
from src.model import IrisClassifier
from src.data_processing import load_iris
import src.config

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    df = load_iris(src.config.datapath)

    X= df. drop(columns="species", axis=1)
    y= df['species']

    # print(X)
    # print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # print(X_train.shape)
    # print(X_test.shape)
    # print(y_train.shape)
    # print(y_test.shape)

    #Model Training
    model = IrisClassifier()
    model.fit(X_train, y_train)

    #prediction
    y_pred =model.predict(X_test)

    # accruacy score
    acc = accuracy_score(y_pred, y_test)
    print("The accuracy using logistic regression model:", acc)

    #save the model
    joblib.dump(model, src.config.MODEL_NAME)

if __name__ == "__main__":
    main()