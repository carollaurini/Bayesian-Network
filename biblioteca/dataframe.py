import pandas as pd
import numpy as np


x= {1: {1: 400, 2: 1000},2: {2: 300}}
print pd.DataFrame.from_dict(x, orient="index")

a = [[0,1,1],[6,0,1]]
c= [[0,0,1],[5,6,7]]
b = {x[0]:x[1] for x in a}
print pd.DataFrame.from_dict(b, orient="index")
print b

print a.map(c)
