import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv('twet2012.txt',sep = '\t')
df=df[(df.Ind==54)|(df.Ind==154)|(df.Ind==254)|(df.Ind==354)|(df.Ind==454)|(df.Ind==554)|(df.Ind==654)|(df.Ind==754)|(df.Ind==854)|(df.Ind==954)|(df.Ind==1054)|(df.Ind==1154)|(df.Ind==1254)|(df.Ind==1354)|(df.Ind==1454)|(df.Ind==1554)|(df.Ind==1654)|(df.Ind==1754)|(df.Ind==1854)|(df.Ind==1954)|(df.Ind==2054)|(df.Ind==2154)|(df.Ind==2254)|(df.Ind==2354)]
df.Ind=df.Ind/100
print df
intpart=[]

for i in df.Ind:
    intpart.append(int(i))
df['Ind']=intpart
df['Date'] = df['Date'].astype(str)+' '+df['Ind'].astype(str)+':00'
df =df.drop('Ind',1)
df=df.set_index('Date')
df.index=df.index.to_datetime()
df.to_csv('twetclean2012.txt',sep = ' ')

