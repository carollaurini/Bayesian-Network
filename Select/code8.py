import pandas as pd
import numpy as np
from Discretization.discretization import *


def selection_table(df,pa,c,method,info):
    v=[]
    v = pa+c  
    array = [list() for _ in xrange(len(v))] # empty array of arrays

    pmax=[] ##pmax = Max Probability
    e=[] ##exp = Expectaion

    for col in df:
        for j in range(len(pa)):
            array[j].append(col[j])
    for col in df:
        pmax.append(df[col].idxmax())
        e.append(sum(df[col]*df.index))

    df1 = pd.DataFrame()
    for i in range(len(pa)):
        df1[pa[i]]=array[i]

    if method=='e':
            if c[0]+'_BN'=='Tset_BN':
                exp = dis_Tset(e)
                df1[c[0]+'_BN'] = exp
            else:
                df1[c[0]+'_BN'] = e
                #df1=dis(df1,info,pa,c)## Load has to be discrete. Check it later
    else:
        df1[c[0]+'_BN'] = pmax
    return df1

def func_select(df,df2,pa,c,method,info):
    pa=[x + '_dis' for x in pa]
    df1 = selection_table(df,pa,c,method,info)
    df2=df2.merge(df1,left_on=pa,right_on=pa,how='left')
    df2=df2.fillna('default')
    df2['Default']=df2[c[0]+'_BN']
    print 'Default Points: '+ str(df2[c[0]+'_BN'].str.contains('d').sum())
    print 'Size of the Testing Set: '+str(len(df2)) 
    if c[0]+'_BN'=='Tset_BN':
        df2=default_tset(df2)
    else:
        default_load(df2)
    #print df2
    return df2
    
def default_tset(df):
    for i in range(len(df)):     
       if df.Tset_BN[i]=='default' and df['Twet'][i]+1.11<=15.11:
           df.Tset_BN[i]=15.11
           continue
       if df.Tset_BN[i]=='default' and df['Twet'][i]+1.11>=26.11:
           df.Tset_BN[i]=26.11
           continue
       elif df.Tset_BN[i]=='default':
           df.Tset_BN[i]=df['Twet'][i]+1.11

    df.Tset_BN=dis_Tset(df.Tset_BN)
    return df
        

def default_load(df):
    k=8400/25
    for i in range(len(df)):     
       if df.Load_BN[i]=='default':
           df.Load_BN[i]=k*df.Twet[i]
    return df


def dis_Tset(h):
    cut = [15.11,15.61,16.61,17.61,18.61,19.61,20.61,21.61,22.61,23.61,24.61,25.61,26.61]
    label = [15.11,16.11,17.11,18.11,19.11,20.11,21.11,22.11,23.11,24.11,25.11,26.11]
    y=pd.cut(h,cut,labels=label,right=False)
    return y

