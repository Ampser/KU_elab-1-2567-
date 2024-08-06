h=int(input("Enter horizontal shift size: "))
v=int(input("Enter vertical shift size: "))
lis=[]
print("Enter image:")
n=0
row=0
while True:
        n= input()
        if n=='-1':break
        lis.append(list(n))
        row+=1
col = len(lis[0])
print("After shift:")
'''for i in range(len(lis)-v):
    for j in range(len(lis[i])-h):
        lis[i+v][j+h]=lis[i][j]
for i in range(row):  
    for j in range(col):
        if i<v or j<h:
            lis[i][j]='0' '''
shifted = [['0'] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        new_i = i + v
        new_j = j + h
        if new_i < row and new_j < col:
            shifted[new_i][new_j] = lis[i][j]
for i in range(row):
    for j in range (col):
        print(shifted[i][j],end='')
    print()
