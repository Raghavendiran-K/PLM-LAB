import numpy as np
import copy as c

CT = {"A":[9,5,8,3,4,1,7],"B":[2,4,10,5,6,11,6]}
l = []
x = c.deepcopy(CT['A'])
l.append(x)
x = c.deepcopy(CT['B'])
l.append(x)
l1 = [[],[]]
k1 = 0
m1 = len(l1[0])


while (len(l[0]) != 0) and (len(l[1]) != 0):
    k = min(l[0])
    m = min(l[1])
    i1 = l[0].index(k)
    i2 = l[1].index(m)
    
    if k >= m:
        l1[0].insert(k1,l[0][i2])
        l1[1].insert(k1,l[1][i2])
        l[0].remove(l[0][i2])
        l[1].remove(l[1][i2])
        k1 += 1
        
    else:
        l1[0].insert(m1,l[0][i1])
        l1[1].insert(m1,l[1][i1])
        l[0].remove(l[0][i1])
        l[1].remove(l[1][i1])
        m1 -= 1

    
l1[1].reverse()
l1[0].reverse()

Index = []
for i in l1[0]:
    Index.append(CT['A'].index(i)+1)
    
def create_table(l,I):
    list1 = []
    for i in range(len(I)):
        k = {'job':I[i],'start':0,'end':0,'mc':'A'}
        m = {'job':I[i],'start':0,'end':0,'mc':'B'}
        list1.append(k)
        list1.append(m)
    return list1

lis = np.array(l)
lis1 = np.array(l1)
        
Table =  create_table(l1,Index)  

for i in range(len(Table)):
    if Table[i]['mc'] == 'A':
        if i == 0:
            Table[i]['end'] += l1[0][0]
           
        else:
            k = int(i/2)
            Table[i]['start'] += Table[i-2]['end']
            Table[i]['end'] = Table[i]['start'] + l1[0][k]
            
    if Table[i]['mc'] == 'B':
        if i == 1:
            Table[i]['start'] += Table[i-1]['end']
            Table[i]['end'] = Table[i]['start'] + l1[1][0]
        else:
            m = int((i-1)/2)
            if Table[i-1]['end'] < Table[i-2]['end']:
                Table[i]['start'] += Table[i-2]['end']
                Table[i]['end'] = Table[i]['start'] + l1[1][m]

print(lis1,Table,sep = '\n\n')
print("\nMachine A idle time:",Table[len(Table)-1]['end']-Table[len(Table)-2]['end'])
print("\nMachine B idle Time:",Table[0]['end']-Table[0]['start'])
            
