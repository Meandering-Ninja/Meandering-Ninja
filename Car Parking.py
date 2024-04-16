import numpy as np
r=int(input("Enter the Number of Rows: "))
c=int(input("Enter the Number of Cols: "))
l=[]
for i in range (r*c):
    x=int(input("Enter elements :"))
    l.append(x)

l1=np.array(l).reshape(r,c)

m=0
k=0
for i in range (r):
    sum=0
    for j in range (c):
        sum+=l1[i][j]
    if(sum>m):
        m=sum
        k=i
print(f'The row with highest number of parked car is {k+1} row')
 
