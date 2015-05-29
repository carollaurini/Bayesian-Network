import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta


df1 = pd.read_csv('power.txt',sep='\t')
df2 = pd.read_csv('Out.txt',sep=' ')

df=df2.join(df1,on='Power', how='right', sort=True,rsuffix='L')
del df['Tset']
df=df.dropna()
df.dropna()
df.index=df.Date
df.index=df.index.to_datetime('%d/%m/%Y %H')
df=df.sort(columns=None,axis=0,ascending=True)
print df
print len(df2)
print len(df)
df.to_csv('2012sen.txt',sep = '\t')
