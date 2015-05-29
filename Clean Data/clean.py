import pandas as pd
import numpy as np


df = pd.read_csv('data.csv',sep=',',na_values=['Unreliable rate','2012'],low_memory =False)
df=df.dropna()
df = df[(df.Reference == 'load')]
df =df.drop(['Reference','Year','Status'],1)
df['Load']= df['Load'].astype(float)
group = df.groupby('Date')
df= 2910*group.mean()
df.to_csv('loadclean.txt',sep = ' ')
