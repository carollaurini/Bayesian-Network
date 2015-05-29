import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import xlsxwriter

def plot_err_curv(dis_rand,err,c,name,d):
    dis_rand=dis_rand.reset_index(drop=True)
    
    a=dis_rand[name][10:d]+dis_rand[name][10:d]*err+c
    b=dis_rand[name][10:d]-dis_rand[name][10:d]*err+c
    plt.plot(dis_rand.index[10:d],dis_rand[name][10:d],label= name+' without Error',linewidth=3,color='black')
    plt.plot(dis_rand.index[10:d],dis_rand[name+'+Err'][10:d],':',linewidth=4,label=name+' with Error',color='black')
    plt.plot(dis_rand.index[10:d],a,'r--',label='Error Boundary',linewidth=3,color='black')
    plt.plot(dis_rand.index[10:d],b,'r--',linewidth=3,color='black')
    plt.ylabel('Cooling Load (Ton)',size=30)
    plt.xlabel('Time (h)',size=30)
    #plt.title('Case 4',size=30)
    legend(fontsize=30,loc='best')
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5,10.5)
    fig.savefig('Error'+name+'.png',dpi=100)
    plt.show()

def func_plot(df,yt,yl):
#Reshapping df
    df=df.fillna(0)
    df=df.stack(level='Load_Dis')
    df=df.reset_index(level='Load_Dis', inplace=False)
    df=df.groupby('Load_Dis')
    c=[]
    d=[]
    for k, group in df:
        c.append(group)
        d.append(k)
    graph = pd.concat(c, ignore_index=False, keys=d)
    graph=graph.drop('Load_Dis',1)
    graph.index.names = ['Load','Tset']
    graph=graph.fillna(0)
    #print graph  
    
# Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('cpd.xlsx', engine='xlsxwriter')
    graph.to_excel(writer, sheet_name='CPD')
    writer.save()  
