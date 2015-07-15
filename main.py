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
    data.to_csv('train.txt',sep='\t')
    return data
def Procedure_Evaluate(cpd,data,errT,errL,number_case,c):
    rand = randon(data,errT,errL,c)
    dis_rand=dis(rand,yt,yl,'Twet+Err','Load+Err','Hour','DayofWeek')
    #print dis_rand
    df_evaluation=func_select(cpd,dis_rand,'Hour','DayofWeek','Twet+Err')
    #ecase=func_error(df_evaluation,'Eval')
    #print 'The error for case '+str(number_case)+': '+str(ecase)
    dis_rand.to_csv('out'+number_case+'.txt',sep = '\t')
    #plot_err_curv(rand,errL,c,'Twet',24)
    
#Discretization of Training Set
data = Procedure_Concat('Train.txt')
datatrain=dis(data,yt,yl,'Twet','Load','Hour','DayofWeek')
#print datatrain
#datatrain.to_csv('Training.txt',sep='\t')

#Discretization of Testing Set
test = Procedure_Concat('Test.txt')
datatest=dis(test,yt,yl,'Twet','Load','Hour','DayofWeek')
#datatest.to_csv('Testing.txt',sep='\t')

#Procedure Training

#BN 1#
#cpd = func_p_Tset1(datatrain)
#print cpd

#BN 2#
cpd2 = func_p_Tset2(datatrain)
##cpd2.to_csv('Table.txt', sep='\t')
#print cpd2

##
####Procedure Evaluation
Procedure_Evaluate(cpd2,datatest,0,0,'no_error',0)
