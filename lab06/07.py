direc=input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))
lis=[]
temp=[]
for i in range (size):
    for j in range (size):
        n= input()
        lis.append(n)
    temp.append(lis)
print (temp)