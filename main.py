import pandas as pd
import numpy as np
import os
from Discretization.discretization import *
from Training.training import *
from Select.code8 import *
from error.error import *
from Randon.randon import *

##Settings##

# 1) Nodes 
#pa=['Load','Twet']
pa=['DayofWeek','Hour','Twet'] #Parent Nodes
#c=['Tset']
c=['Load'] #Child Node

# 2) Method os extimation
method='e' #Expectation (e) or Max probability (pmax)

# 3) Discretization Setting
#info =[[0,3000,50],[10.0,25.0,1.0],['NaN']]
info=[['NaN'],['NaN'],[5,30.0,5.0],[0,3000,50]] #[[Begin,End,Step],...,[Begin,End,Step]]

# 4)Name of the file out
model ='model_3.2'

############

## Month Concatenation Function:
def Procedure_Concat(fi):
    File = open(fi,'r')
    filelist = File.read().split('\n')  
    data=[]    
    for month in filelist:
        df_month = pd.read_table(month+'.txt',sep='\t')
        data.append(df_month)
    data = pd.concat(data, ignore_index=False, keys=filelist)
    #data.to_csv('train_data.txt',sep='\t')
    return data

#### Evaluation Function:
def Procedure_Evaluate(cpd,data,method,model,c):  
    df_evaluation=func_select(cpd,data,pa,c,method,info)
    df_evaluation.to_csv('out'+model+'.txt',sep = '\t')
    func_error(df_evaluation,c) #Root Square

    
#### Discretization of Training Set
data = Procedure_Concat('Train.txt')
datatrain=dis(data,info,pa,c)
#print datatrain.head(20)
#datatrain.to_csv('Training.txt',sep='\t')

#### Discretization of Testing Set
test = Procedure_Concat('Test.txt')
datatest=dis(test,info,pa,['NaN'])############
#print datatest.head(20)
#datatest.to_csv('Testing.txt',sep='\t')

#### Procedure Training
cpd = training(datatrain,pa,c)
#print cpd
#### Procedure Evaluation
Procedure_Evaluate(cpd,datatest,method,model,c)
