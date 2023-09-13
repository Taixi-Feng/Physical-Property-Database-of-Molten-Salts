import pandas as pd
import os
import shutil
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import joblib
#Self-coefficients
# Datasets directory
data_dir = "./Self-coefficient/"
datas_scs = os.listdir(data_dir)
print(datas_scs)
# Initial Scalers and models
scalers = {}
models = {}
# Deal with datasets
for data_sc in datas_scs:
    # read datasets
    data = pd.read_csv(os.path.join(data_dir, data_sc)) 
    # Split datasets
    x_train = data.iloc[:, :2]
    print(x_train.shape)
    for i in range(3):
        y_train = data.iloc[:, [i+2]]
        # Training model
        model = Ridge(alpha=0.01,random_state=8,max_iter=1000)
        model.fit(x_train, y_train)
        models[data_sc] = model  # Store model
        # Evaluate model
        train_score = model.score(x_train, y_train) 
        # Store file
        with open(f"Score[{data_sc}-{i}].txt", 'a') as file:
            file.write(f"Train Score: {train_score}\n")   
        # Remove
        shutil.move(f"Score[{data_sc}-{i}].txt", data_dir)
        # Store model file
        joblib_file = f"./Self-coefficient/joblib_model[{data_sc}-{i}].pkl"
        joblib.dump(model, joblib_file)