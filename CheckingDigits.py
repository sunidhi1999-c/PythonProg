# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:33 2021

@author: HP
"""

"""
program to check if input contains only numeric digit or not
i/p:"1234" INFYTQ
o/p:true
i/p:2FSd
o/p:false
the CODE:
string=input()
for digit in string:
    if digit not in "123456789":
        print("No")
    else:
        print("Yes")
        
"""      
def isodd(num):
    return int(num)%2
#2 approach
#isdigit()
#list1=[2,4,6,8,10,12]
list1=list(map(isodd,input().strip().split()))
#for ele in list1:
 #   if ele%2==0:
  #      print("Yes")
    #    break
   # else:
     #   print("No")
  
print("yes" if all(list1) else "NO")