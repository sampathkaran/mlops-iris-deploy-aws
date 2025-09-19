# This file is to create foler and files programatically

import os

folder_files_list = [
        "src/",
        "src/model.py",
        "src/data_preprocessing.py",
        "src/utils.py",
        "src/__init__.py",
        "tests/",
        "tests/test_model.py",
        "tests/test_data_preprocessing.py",
        "tests/test_utils.py",
        "model/",
        "data/",
        "data/raw/",
        "data/processed/",
        "requirements.txt",
        "train.py",
        "predict.py",
        "config.py",
        "DockerFile"
]

for path in folder_files_list:
    folder_path, file_path = os.path.split(path)
    if folder_path != "":
        os.makedirs(folder_path, exist_ok=True) # exist_ok True will not throw an error if exists
    if file_path != "":
        filenamepath = os.path.join(folder_path, file_path)
        with open(filenamepath, 'w') as f:
            pass
    else:
        pass