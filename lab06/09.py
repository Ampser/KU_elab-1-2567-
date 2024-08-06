n = int(input("Enter the number of rows or columns : "))
for i in range (n):
    for j in range(n):
            if(j<10):
                print(f'%{((j)//10)+2}d'%(j+1+i),end=" ")
            else:print(f'%{((j)//10)+1}d'%(j+1+i),end=" ")
    print()