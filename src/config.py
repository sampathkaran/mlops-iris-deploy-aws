import os
from pathlib import Path
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
data_file_name = "iris.csv"
datapath = os.path.join(PACKAGE_ROOT,"data", "raw", data_file_name)
#print (datapath)
MODEL_NAME = "model/iris_model.joblib"