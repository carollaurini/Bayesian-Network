import pandas as pd
import numpy as np
import info

def dis(month,yt,yl,column1,column2):
    month[column1+'_Dis'] = pd.cut(month[column1],yt, labels = range(len(yt)-1),right=False) 
    month[column2+'_Dis'] = pd.cut(month[column2],yl, labels = range(len(yl)-1),right=False) 
    return month
