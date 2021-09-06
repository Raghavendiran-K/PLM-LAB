# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 23:54:56 2021

@author: K Raghavendiran
"""
# Least cost method
def creatematrix(x,y,z):
    A = []
    for i in range(3):
        k = []
        for j in range(4):
            d = {}
            d['cost'] = x[i][j]
            d['units'] = 0
            k.append(d)
        k.append(y[i])
        A.append(k)
    A.append(z)
    return A
            
cost_matrix = [[2,3,11,7],[1,0,6,1],[5,8,15,9]]
supply_matrix = [6,1,10]
demand_matrix = [7,5,3,2,17]
MATRIX = creatematrix(cost_matrix,supply_matrix,demand_matrix)
x = []
for i in range(3):
    for j in range(4):
        x.append([cost_matrix[i][j],i,j])
x.sort()

def processing(A,k):
    while len(k)!=0:
        r = k[0][1]
        c = k[0][2]
        l = len(A)-1
        m = len(A[r])-1
        
        if len(k)>1:
            r1 = k[1][1]
            c1 = k[1][2]
            if k[0][0] == k[1][0]:
                diff0 = abs(A[r][m]-A[l][c])
                diff1 = abs(A[r1][m]-A[l][c1])
                if diff1 > diff0:
                    temp = k[0]
                    k[0] = k[1]
                    k[1] = temp
            
        if A[r][m] > 0 and A[l][c] > 0 and A[r][m] >= A[l][c]:
            A[r][c]['units'] += A[l][c]
            A[r][m] -= A[l][c]
            A[l][c] -= A[l][c]
        
        if A[r][m] > 0 and A[l][c] > 0 and A[r][m] < A[l][c]:
            A[r][c]['units'] += A[r][m]
            A[l][c] -= A[r][m]
            A[r][m] -= A[r][m]
        k.remove(k[0])
    
    return A

MATRIX = processing(MATRIX, x)

TOTAL_COST = 0
for i in range(len(MATRIX)-1):
    for j in range(len(MATRIX[i])-1):
        TOTAL_COST += (MATRIX[i][j]['cost']*MATRIX[i][j]['units'])

print("TOTAL COST is RS",TOTAL_COST*100)
      
        
        


    
          
