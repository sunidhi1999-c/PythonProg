# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:13:25 2021

@author: HP
"""
#infytq NUMBER SEQUENCE
#to convert float,int input to numbers
def convert(data):
   if "." in data:#float
       return float(data)
   else :
        return int(data)
#return float(data)if "." in data else int(data)
#numlist=[int(ele) for ele in input().split(",")]
numlist=list(map(convert,input().split(",")))

print(numlist)
num1=numlist[:numlist.index(5)+numlist[numlist.index(8)+1:]]
list1=numlist [numlist.index(5):numlist.index(8)+1]
#print(list1)
numstr=""
for ele in list1:
    numstr+=str(ele)
print(int(numstr)+num1)