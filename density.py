import pandas as pd
import os
import shutil
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import joblib

# Datasets directory
data_dir = "./Density/"
datas_density = os.listdir(data_dir)

# Initial Scalers and models
scalers = {}
models = {}

# Deal with datasets
for data_density in datas_density:
    # read datasets
    data = pd.read_csv(os.path.join(data_dir, data_density))   
    # Split datasets
    x_train = data.iloc[:, :2]
    y_train = data.iloc[:, 2:]
    # Training model
    model = Ridge(alpha=0.01,random_state=8,max_iter=1000)
    model.fit(x_train, y_train)
    models[data_density] = model  # Store model
    # Evaluate model
    train_score = model.score(x_train, y_train) 
    # Store file
    with open(f"Score[{data_density}].txt", 'a') as file:
        file.write(f"Train Score: {train_score}\n")   
    # Remove
    shutil.move(f"Score[{data_density}].txt", data_dir)
    # Store model file
    joblib_file = f"./Density/joblib_model[{data_density}].pkl"
    joblib.dump(model, joblib_file)
