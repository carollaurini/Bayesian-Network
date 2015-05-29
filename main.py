import pandas as pd
import numpy as np
import os
from Discretization.discretization import *
from Training.training import *
from Select.code8 import *
from error.error import *
#from Plot.plot import *
from Randon.randon import *
import info

xt = np.append(np.arange(info.bT,info.eT+info.spT,info.spT),1000000000)
yt = np.append(-100000000,xt)
xl = np.append(np.arange(info.bL,info.eL+info.spL,info.spL),1000000000)
yl = np.append(-100000000,xl)

print yl
print yt

def Procedure_Concat(fi):
    File = open(fi,'r')
    filelist = File.read().split('\n')  
    data=[]    
    for month in filelist:
        df_month = pd.read_table(month+'.txt',sep='\t')
        data.append(df_month)
    data = pd.concat(data, ignore_index=False, keys=filelist)
    #print data
    return data

def Procedure_Evaluate(data,errT,errL,number_case,c):
    rand = randon(data,errT,errL,c)
    dis_rand=dis(rand,yt,yl,'Twet+Err','Load+Err')
    print dis_rand
    df_evaluation=func_select(cpd,dis_rand,'Twet+Err','Load+Err')
    #ecase=func_error(df_evaluation,'Eval')
    #print 'The error for case '+str(number_case)+': '+str(ecase)
    dis_rand.to_csv('case'+number_case+'.txt',sep = '\t')
    #plot_err_curv(rand,errL,c,'Twet',24)
    
#Discretization of Training Set
#data = Procedure_Concat('Train.txt')
data = pd.read_table('Out.txt',sep=' ')
datatrain=dis(data,yt,yl,'Twet','Load')
#datatrain.to_csv('Training.txt',sep='\t')

#Discretization of Testing Set
test = Procedure_Concat('Test.txt')
datatest=dis(test,yt,yl,'Twet','Load')
#datatest.to_csv('Testing.txt',sep='\t')

#Procedure Training
cpd = func_p_Tset(datatrain)
#print cpd

##Procedure Evaluation
Procedure_Evaluate(datatest,0,0,'no_error',0)
#Procedure_Evaluate(datatest,1,0.2,'witherror',4)
#Procedure_Evaluate(test,1,0.2,'2',0)
#Procedure_Evaluate(test,1,0.1,'3',0)
#Procedure_Evaluate(test,0,0,'4',0)
