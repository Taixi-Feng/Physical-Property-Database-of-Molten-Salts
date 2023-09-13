import joblib
import pandas as pd
def Model_predict_1(T,System,N,target):
    Target=target.title()
    Model=joblib.load(f'./{Target}/joblib_model[{Target}({System}).csv].pkl')
    x_predict=pd.DataFrame([[N,T]])
    prediction = Model.predict(x_predict)
    return prediction
def make_i(System,target_ion):
    if "Li" in System and "Na" in System:
        if target_ion == 'Li+':
            i=0
        elif target_ion == 'Na+':
            i=1
        else:
            i=2
    elif "Li" in System and "K" in System:
        if target_ion == 'Li+':
            i=0
        elif target_ion == 'K+':
            i=1
        else:
            i=2
    elif "Na" in System and "K" in System:
        if target_ion == 'Na+':
            i=0
        elif target_ion == 'K+':
            i=1
        else:
            i=2
    return i
def Model_predict_2(T,System,N,target,i):
    Target=target.title()
    Model=joblib.load(f'./{Target}/joblib_model[{Target}({System}).csv-{i}].pkl')
    x_predict=pd.DataFrame([[N,T]])
    prediction = Model.predict(x_predict)
    return prediction