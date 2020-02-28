# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:02:38 2020

@author: 212560141
"""
# Question 3
# Creating Corrupted data set
for x  in range(1,33):
    import random
    cluster = [random.random() for i in range(1,17)]
    cluster[9] = "err" 
    cluster[9] = 2
    clusterSensor  = [random.random() for i in range(1,17)]
    A = ('cluster no:', x,cluster)
    print(A)
   
    
    
#Function to test for Error  
 # code to detect where the error in the data set is   
acceptable_range = range(0,1)
def my_func(clusterSensor):
  for i in range(len(clusterSensor)):
    clusterSensor = clusterSensor[i]
    print (i, clusterSensor) #code to print where the err location in the data se