import pandas as pd
import numpy as np
import info

month = pd.read_table ('Jun.txt',sep=' ')

#Twet Discretization , 27 bins, space= 1, begin = 0, end = 25
x = np.append(range(0,25+1,1), max(month['Twet'])+0.1)
y = np.append(min(month['Twet'])-0.1,x)

month['Twet'] = pd.cut(month.Twet,y, labels = range(0,27),right=False)


#Load Discretization , 10 bins, space 216, begin 234 , end= 1972
x = np.append(range(234,1972+216,216), max(month['Load'])+0.1)
y = np.append(min(month['Load'])-0.1,x)

month['Load'] = pd.cut(month.Load,y, labels = range(0,10),right=False)



month = month[['Twet','Load','Tset']].astype(int)
month = month.sort(columns = 'Twet')
month = month.set_index(['Twet'])

print month
