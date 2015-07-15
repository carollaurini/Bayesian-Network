import pandas as pd
import numpy as np

def split(year):

    df = pd.read_table(year+'_out.txt',sep='\t')
    df=df.set_index('Date')
    df.index=df.index.to_datetime()
    df['Hour']=df.index.hour
    df['month']= df.index.month
    df['DayofWeek']= df.index.dayofweek
    g=df.groupby('month')
    for k,group in g:
        group.to_csv(str(k)+'_'+year+'.txt', sep='\t')
    print df
split('2011')
split('2012')
split('2013')
