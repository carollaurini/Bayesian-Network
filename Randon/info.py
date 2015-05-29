import pandas as pd

binT=27
binL=10    
spT=1
spL=200
bT=0
bL=200
eT=25
eL=2000
df= pd.read_table ('input.txt',sep='\t')
min_Twet = min(df.Twet)
min_Load = min(df.Load)
max_Twet = max(df.Twet)
max_Load = max(df.Load)

