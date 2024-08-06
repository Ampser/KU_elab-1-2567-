row = int(input("Enter Rook's row position: "))
col = int(input("Enter Rook's column position: "))
for i in range(8):
    print('-----------------')
    for j in range(8):
        if(i==row and j==col):
            print("|R",end='')
            continue
        if(i==row or j==col):
            print("|x",end='')
        else: print("| ",end='')
    print("|")
print("-----------------")
