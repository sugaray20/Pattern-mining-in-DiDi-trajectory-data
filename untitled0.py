# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:24:27 2019

@author: sugaray
"""
b=["Jul","Aug","Sep","Oct","Nov","Dec"]
c=[]

for i in range(30):
    c.append(str(i+1).zfill(2))
    
a=[]
for i in range(6):
    for j in range(30):
        a.append("%"+"%s %s"%(b[i],c[j])+"%")
        
a.insert(0,"%Jun 30%")
a.insert(31,"%Jul 31%")
a.insert(62,"%Aug 31%")
a.insert(123,"%Oct 31%")
a.insert(184,"%Dec 31%")


