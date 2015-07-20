import pandas as pd
import numpy as np

def training(ld2,pa,c):
    p=[]
    v=[]
    pa=[x + '_dis' for x in pa]
    c=[x + '_dis' for x in c]
    v = pa+c
    array = [list() for _ in xrange(len(v))] # empty array of arrays
    #print ld2
    ld2 = ld2.groupby(v)    
    for k,group in ld2:
        for i in range(len(v)):
            array[i].append(k[i])
        p.append(len(group))

    df = pd.DataFrame()
    for i in range(len(v)):
        df[v[i]]=array[i]
    df['P'] = p
    #print df
    df1 = pd.pivot_table(df, values='P',index=c,columns=pa)
    df1=df1.fillna(0)
    
    for i in df1:
        df1[i]=df1[i]/sum(df1[i])
    #print df1   
    return df1


