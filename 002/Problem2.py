# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:38:31 2018

@author: Adam
"""


SeqStop=4*10**6
FibSeq=[1,2]
FibSeqEven=[2]
Flag=1
i=2
while (Flag):
    FibSeq.insert(i,FibSeq[i-1]+FibSeq[i-2])
        
    if FibSeq[i]<=SeqStop and FibSeq[i] % 2 == 0:
        FibSeqEven.insert(-1,FibSeq[i])
        
    if FibSeq[i]>=SeqStop: 
        Flag=0
    i=i+1
        
print(sum(FibSeqEven))