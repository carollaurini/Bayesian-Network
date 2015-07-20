import pandas as pd
import numpy as np

def dis(data,info,pa,c):
    v=pa+c
    if c[0]=='NaN':
        v=pa
    #print v
    for i in range(len(v)):
        if info[i][0]=='NaN':
            data[v[i]+'_dis']=data[v[i]]
        else:
            x=[]
            y=[]
            x = np.append(np.arange(info[i][0],info[i][1]+info[i][2],info[i][2]),1000000000)
            y = np.append(-100000000,x)
            #print x
            data[v[i]+'_dis'] = pd.cut(data[v[i]],y, labels = np.arange(info[i][0],info[i][1]+2*info[i][2],info[i][2]),right=False)
    return data


