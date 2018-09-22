# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:41:22 2018

@author: Adam
"""
from timeit import default_timer as timer

CorrectVal=267330

start=timer()
def FindMult(MaxNum, Multplier):
    flag=1
    All=[]
    Multiples=[]
    i=1
    while (flag):
        CurVal=i*Multplier
        All.insert(i,CurVal)
        if CurVal<MaxNum:
            flag=1 
            Multiples.insert(i, CurVal)
            i=i+1
        else:
                flag=0
    
    MultSum=sum(Multiples)            
  #  print(MultSum)
    return MultSum, All;

MaxNum=10**7
Multplier=5
[Mult5Sum,All5]=FindMult(MaxNum,Multplier)


Multplier=3
[Mult3Sum,All3]=FindMult(MaxNum,Multplier)

stop=timer()
ElapsedTime=stop-start

TotalSum=Mult3Sum+Mult5Sum

print(ElapsedTime)
print(TotalSum," Right Anser:",CorrectVal)