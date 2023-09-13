import pandas as pd
import os
import shutil
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import joblib
#Viscosity
# Datasets directory
data_dir = "./Viscosity/"
datas_viscosity = os.listdir(data_dir)
# Initial models
models = {}
# Deal with datasets
for data_viscosity in datas_viscosity:
    # read datasets
    data = pd.read_csv(os.path.join(data_dir, data_viscosity))   
    # Split datasets
    x_train = data.iloc[:, :2]
    y_train = data.iloc[:, 2:] 
    # Training model
    model = Ridge(alpha=0.01,random_state=8,max_iter=1000)
    model.fit(x_train, y_train)
    models[data_viscosity] = model  # Store model
    # Evaluate model
    train_score = model.score(x_train, y_train) 
    # Store file
    with open(f"Score[{data_viscosity}].txt", 'a') as file:
        file.write(f"Train Score: {train_score}\n")   
    # Remove
    shutil.move(f"Score[{data_viscosity}].txt", data_dir)
    # Store model file
    joblib_file = f"./Density/joblib_model[{data_viscosity}].pkl"
    joblib.dump(model, joblib_file)