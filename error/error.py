import pandas as pd
import numpy as np
import math 

def func_error(df,name):
    df['error']= df['Tset']- df['Tset_BN']
    df['error'] = df['error'].abs()
    df['error'] = df['error']/df['Tset']
    #df.to_csv(name+'.txt',sep='\t')
    e = df['error'].sum()
    e = 100*(e/len(df['Tset']))#Sample Size
    return e
