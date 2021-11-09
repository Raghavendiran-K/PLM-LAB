# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:50:28 2021

@author: K Raghavendiran
"""
import copy 
import numpy as np
matrix_original = [[20,36,31,27],[24,34,45,22],[22,45,38,18],[37,40,35,28]]
matrix = copy.deepcopy(matrix_original)
a = np.array(matrix)
print("Initial cost matrix:\n",a,"\n")
#Iteration 1 and 2
def minlist(l):
    mi = []
    for i in range(len(l)):
        minimum = l[i][0]
        for j in range(len(l[i])):
            if l[i][j]<minimum:
                minimum =l[i][j]
        mi.append(minimum)
    return mi

def processing(l,k):
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] -= k[i]
    return(l)

def transpose(l):
    for i in range(len(l)):
        temp = 0
        for j in range(len(l[i])):
            if j>=i:
                temp = l[i][j]
                l[i][j] = l[j][i]
                l[j][i] = temp
    return l

min_list = minlist(matrix)
matrix = processing(matrix,min_list)

matrix = transpose(matrix)
min_list = minlist(matrix)
matrix = processing(matrix,min_list)
matrix =transpose(matrix)
b = np.array(matrix)
print("Matrix after Iteration 1 & 2:\n",b,"\n")


index = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
                index.append([i,j])
                for k in range(i,len(matrix)):
                    matrix[k][j] = -1
                for m in range(j,len(matrix[i])):
                    matrix[i][m] = -1
                    
total = 0
for i in index:
    total = total + matrix_original[i[0]][i[1]]
print("Total cost:",total)
    


                    
            
            
            
            
            
        
    