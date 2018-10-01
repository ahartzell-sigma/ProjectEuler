# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:17:36 2018

@author: AHartzell
"""
SmallestNum=10
NumRange=list(range(1,SmallestNum+1))

i=1
Flag=1
TruthTable=[]
while (Flag):
    
    for x in NumRange:
        print(x)
        if SmallestNum % NumRange[x] == 0:
            TruthTable.insert(x,True)
        else: 
            TruthTable.insert(x,False)
            
        if all(TruthTable)==True :
            Flag=0
            print(i)
            
    i=i+1
            
    

        
