import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm

def selection_table(df):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    
    df=df.fillna(0)  
    for i in df:
        s=0
        a.append(i[0])
        b.append(i[1])
        c.append(i[2])
    for col in df:
        d.append(df[col].idxmax())
        e.append(sum(df[col]*df.index))
    
    exp = dis_Tset(e)
    
    df1 = pd.DataFrame()
    df1['Hour'] = a
    df1['DayofWeek'] = b
    df1['Twet'] = c
    df1['Tset'] = exp  ## d = Max Probability , exp = Expectaion
    return df1

def func_select(df,df2,column1,column2,column3):    
    df1 = selection_table(df)
    df2['Default']=df2[column1+'_Dis'].astype(str) #Just creating a column 'Default'
    h=[]
    n=0
    df1.to_csv('IndexTable.txt',sep='\t')
    for i in range(len(df2[column2])):
                   aux=0
                   for j in range(len(df1['Tset'])):
                            if df2[column1+'_Dis'][i]==df1['Hour'][j] and df2[column2+'_Dis'][i]==df1['DayofWeek'][j] and df2[column3+'_Dis'][i]==df1['Twet'][j]and df2['Twet'][i]<df1['Tset'][j]:
                                h.append(df1['Tset'][j])
                                df2['Default'][i]='No'
                                aux=1
                                break
                            else:
                                aux=0
                                df2['Default'][i]='Yes'
                            
                                
                   if aux==0:
                       n=n+1
                       if df2[column1][i]+1.11<=15.11:
                           h.append(15.11)
                           continue
                       if df2[column1][i]+1.11>=26.11:
                           h.append(26.11)
                           continue
                       else:
                           h.append(df2[column1][i]+1.11)
                           
    df2['Tset_BN']=h
    
    df2['Tset_BN']=dis_Tset(df2['Tset_BN'])
    print 'Number of default points is: '+str(n)
    return df2


def dis_Tset(h):
    cut = [15.11,15.61,16.61,17.61,18.61,19.61,20.61,21.61,22.61,23.61,24.61,25.61,26.61]
    label = [15.11,16.11,17.11,18.11,19.11,20.11,21.11,22.11,23.11,24.11,25.11,26.11]
    y=pd.cut(h,cut,labels=label,right=False)
    return y

    
