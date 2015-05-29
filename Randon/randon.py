import pandas as pd
import numpy as np

def randon(data,errT,errL,c):
    data['Load'].astype(float)
    data['Twet'].astype(float)
    data['Twet+Err']=data['Twet']
    data['Load+Err']=data['Load']
    for i in range(len(data['Twet'])):
        data['Twet+Err'][i] = data['Twet'][i] + np.random.uniform(-errT,errT)+c
        data['Twet+Err'][i]=np.around(data['Twet+Err'][i],decimals=2)
        data['Load+Err'][i] = data['Load'][i] + np.random.uniform(-errL,errL)*data['Load'][i]
        data['Load+Err'][i]=np.around(data['Load+Err'][i],decimals=2)
    return data
