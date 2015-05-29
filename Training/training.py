import pandas as pd
import numpy as np

# Calculation of Probability Twet
def func_p_Twet(tw):
    tw = tw.groupby(['Twet_Dis'])
    pTwet=[]
    cTwet=[]
    for k,group in tw:
        x= len(group)
        h = (x/float(len(df['Twet_Dis'])))
        pTwet.append([k,h])
        cTwet.append([k,x])
    return pTwet
    return cTwet    

###Calculation of Probability Load given Twet
def func_p_Load(ld):
    ld = ld.groupby(['Twet_Dis','Load_Dis'])
    x=[]
    for k,group in ld:
        x.append(k[0])
        x.append(k[1])
        x.append(len(group))
    df1 = pd.DataFrame(columns=range(27),index=range(11))

    for i in range(0,len(x),3):
        #print x[i],x[i+1],x[i+2]
        df1[x[i]][x[i+1]]=x[i+2]
        
    for i in df1:
        df1[i][10]=df1[i].sum()
        df1[i]=df1[i]/df1[i][10]
    return df1

#Calculation of Probability Tset given Load and Twet
def func_p_Tset(ld1):
    ld1 = ld1.groupby(['Twet_Dis','Load_Dis','Tset'])
    y=[]
    a=[]
    b=[]
    c=[]

    for k,group in ld1:
        a.append(k[0])
        b.append(k[1])
        c.append(k[2])
        y.append(len(group))
    df2 = pd.DataFrame()
    df2['Twet_Dis'] =a
    df2['Load_Dis'] =b
    df2['Tset'] =c
    df2['P'] =y
    df2 = pd.pivot_table(df2, values='P',index='Tset',columns=['Load_Dis','Twet_Dis'])
    for i ,j in df2:
        a=df2[i][j].sum()
        df2[i][j]=df2[i][j]/a
    return df2







