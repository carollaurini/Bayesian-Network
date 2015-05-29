import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta


df1 = pd.read_csv('loadclean.txt',sep=' ',index_col = 'Date')
df2 = pd.read_csv('twetclean2012.txt',sep=' ',index_col = 'Date',na_values=['M'])


df=df2.join(df1, how='inner')
df.index=df.index.to_datetime('%d/%m/%Y')
df=df.sort(columns=None,axis=0,ascending=True)
hours = df.index.hour
df= pd.concat([df, pd.DataFrame({'Hour(s)': hours}, index=df.index)], axis = 1)
df['Hour(s)']=df['Hour(s)']*3600
index=pd.DatetimeIndex(df.index)
df['TimeStamp(s)']=index.astype(np.int64)//10**9
print df
print len(df2)
df.to_csv('2012.txt',sep = '\t')
