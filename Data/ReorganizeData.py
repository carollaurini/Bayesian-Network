import pandas as pd
import numpy as np

def split(year):

    df = pd.read_table(year+'_out.txt',sep='\t')
    df=df.set_index('Date')
    df.index=df.index.to_datetime()
    df['month']= df.index.month
    g=df.groupby('month')
    for k,group in g:
        group.to_csv(str(k)+'_'+year+'.txt', sep='\t')
    
split('2011')
split('2012')
split('2013')
