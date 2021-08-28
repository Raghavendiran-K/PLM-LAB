# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:17:52 2021

@author: K Raghavendiran
"""
import xlsxwriter as x
import string as s


'''
#input of variables    
MPS = {}
for i in range(1,9):
    MPS[str(i)] = 0
print("Enter the weeks with non-zero demands(in comma separated):")
L = input().split(',')
m = 0
for i in L:
    m = int(input(f"ENTER THE VALUE OF DEMAND IN WEEK {i} :"))
    MPS[i] += m
MPS_VALUES = list(MPS.values())
MPS_KEYS = list(MPS.keys())

Onhand_Inventory = {}
k = ["Chair","Seat","Back","Leg"]
for i in k:
    Onhand_Inventory[i] = int(input(f"Enter inventory for {i}:"))
OHI_VALUES = list(Onhand_Inventory.values())
OHI_KEYS = list(Onhand_Inventory.keys())
    
Scheduled_reciept = {}
a = ["Chair","Seat","Back","Leg"]
for i in a:
    Scheduled_reciept[i]=int(input(f"Enter Scheduled reciept for {i}:"))
SR_VALUES = list(Scheduled_reciept.values())
SR_KEYS = list(Scheduled_reciept.keys())
'''

# sample values for test
MPS = {'1': 150, '2': 0, '3': 70, '4': 0, '5': 175, '6': 0, '7': 90, '8': 60} 
Onhand_Inventory = {'Chair': 260, 'Seat': 60, 'Back': 40, 'Leg': 80}
Scheduled_reciept = {'Chair': 0, 'Seat': 50, 'Back': 10, 'Leg': 0}

MPS_VALUES = list(MPS.values())
MPS_KEYS = list(MPS.keys())
OHI_VALUES = list(Onhand_Inventory.values())
OHI_KEYS = list(Onhand_Inventory.keys())
SR_VALUES = list(Scheduled_reciept.values())
SR_KEYS = list(Scheduled_reciept.keys())


#file writing in python

excel = x.Workbook("BOM.xlsx")
bold = excel.add_format({'bold':True})
ws = excel.add_worksheet("INPUT PARAMETERS")
ws.set_column('A:A',30)
ws.set_column('B:B',12)
ws.write(0,0,"WEEK",bold)
ws.write(1,0,"DEMANDS",bold)
for i in range(1,9):
    ws.write(0,i,i)
    ws.write(1,i,MPS[str(i)])
ws.write(3,0,"ON-HAND INVENTORY",bold)
ws.write(3,1,"QUANTITY")
for i in range(0,len(OHI_KEYS)):
    ws.write(i+4,0,OHI_KEYS[i])
    ws.write(i+4,1,OHI_VALUES[i])
    
ws.write(9,0,"SCHEDULED RECIEPT FOR WEEK 1",bold)
ws.write(9,1,"QUANTITY")
for i in range(0,len(SR_KEYS)):
    ws.write(i+10,0,SR_KEYS[i])
    ws.write(i+10,1,SR_VALUES[i])
    
def Formatting(A):
    global U 
    U = list(s.ascii_uppercase)
    A.write("A1","item:Chair",bold)
    A.write("B1","Overdue",bold)
    A.set_column("A:A",30)
    content = ["Gross Requirement (GR)","Scheduled Receipt (SR)","Projected On Hand (PoH)","Projected Net Requirement (PNR)","Planned Order Receipt (PORpt)","Planned Order Release (PORel)"]
    for i in range(1,9):
        A.write(f"{U[i+1]}1",f"WEEK {i}",bold)
    row = 1
    coloumn = 0
    for item in content:
        A.write(row,coloumn,item,bold)
        row += 1

w1 = excel.add_worksheet("CHAIR")
Formatting(w1)

w2 = excel.add_worksheet("SEAT")
Formatting(w2)

w3 = excel.add_worksheet("BACK")
Formatting(w3)

w4 = excel.add_worksheet("LEGS")
Formatting(w4)

w5 = excel.add_worksheet("SUMMARY")
w5.write("A1","SUMMARY SHEET(PORel)",bold)
w5.set_column("A:A",25)
w5.write("B1","Overdue",bold)
for i in range(1,9):
    w5.write(f"{U[i+1]}1",f"WEEK {i}",bold)
row = 1
coloumn = 0
for i in range(len(SR_KEYS)):
    w5.write(row,coloumn,SR_KEYS[row-1])
    row += 1


def processing(A):
    for i in range(1,9):
        if A[2][i-1] + A[1][i]  - A[0][i] >= 0:
            A[2][i] += abs(A[2][i-1] + A[1][i]  - A[0][i])
        elif A[2][i-1] + A[1][i]  - A[0][i] < 0:
            x = abs(A[2][i-1] + A[1][i]  - A[0][i])
            A[5][i-2] = x
            A[4][i] = x
            A[2][i] = A[4][i] + A[2][i-1] - A[0][i]
    for i in range(9):
        A[3][i] = A[4][i]
    return A
    
def initialize(A,s):
    for i in range(5):
        k = []
        for j in range(9):
            if i == 0 and j == 1:
                k.append(SR_VALUES[s])
            if i == 1 and j == 0:
                k.append(OHI_VALUES[s])
            else:
                k.append(0)
        A.append(k)
    return A
        
l = [0]
for i in range(len(MPS_VALUES)):
    l.append(MPS_VALUES[i])
C_V = [l]
C_V = initialize(C_V,0)
C_V = processing(C_V)


S_V = [C_V[5]]
S_V = initialize(S_V,1)
S_V = processing(S_V)
    
B_V = [C_V[5]]
B_V = initialize(B_V,2)
B_V = processing(B_V)

L_V =[]
k = [0]
for i in range(9):
    k.append(4*C_V[5][i])
L_V.append(k)
L_V = initialize(L_V,3)
L_V = processing(L_V)


for i in range(6):
    for j in range(9):
        w1.write(i+1,j+1,C_V[i][j])
        w2.write(i+1,j+1,S_V[i][j])
        w3.write(i+1,j+1,B_V[i][j])
        w4.write(i+1,j+1,L_V[i][j])

for i in range(9):
    w5.write(1,i+1,C_V[5][i])
    w5.write(2,i+1,S_V[5][i])
    w5.write(3,i+1,B_V[5][i])
    w5.write(4,i+1,L_V[5][i])
     
excel.close()






    
        
    
