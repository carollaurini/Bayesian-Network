import pandas as pd
import numpy as np
import math 

def func_error(df,c):
    print 'The child node is: '+str(c[0])
    df['error']= pow(df[c[0]]- df[c[0]+'_BN'],2)
    e = (df['error'].sum())/len(df)
    e = np.sqrt(e)
    print 'The RSMD is: '+str(e)
    return e

#df=pd.read_csv('outno_error.txt',sep='\t')
#func_error(df)
