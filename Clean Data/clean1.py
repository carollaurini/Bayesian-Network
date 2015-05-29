import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv('twet11.txt',sep = '\t')
df=df[(df.Ind==53)|(df.Ind==153)|(df.Ind==253)|(df.Ind==353)|(df.Ind==453)|(df.Ind==553)|(df.Ind==653)|(df.Ind==753)|(df.Ind==853)|(df.Ind==953)|(df.Ind==1053)|(df.Ind==1153)|(df.Ind==1253)|(df.Ind==1353)|(df.Ind==1453)|(df.Ind==1553)|(df.Ind==1653)|(df.Ind==1753)|(df.Ind==1853)|(df.Ind==1953)|(df.Ind==2053)|(df.Ind==2153)|(df.Ind==2253)|(df.Ind==2353)]
df.Ind=df.Ind/100
intpart=[]

for i in df.Ind:
    intpart.append(int(i))
df['Ind']=intpart
df['Date'] = df['Date']+' '+df['Ind'].astype(str)+':00'
df =df.drop('Ind',1)
df=df.set_index('Date')
print df
df.to_csv('twetclean.txt',sep = ' ')

