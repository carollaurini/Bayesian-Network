import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import axes3d

df=pd.read_csv('Out.txt',sep=' ')
#print df
fig= plt.figure().gca(projection='3d')
fig.scatter(df.Twet,df.Load,df.Tset)
fig.set_xlabel('Twet ($^\circ$C)',size=30)
fig.set_ylabel('Load (Ton)',size=30)
fig.set_zlabel('Tset ($^\circ$C)',size=30)

plt.show()
