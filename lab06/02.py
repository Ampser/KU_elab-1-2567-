text = input("Input sentence: ")
row =int(input("Input row: "))
i =0
ans=[""]*row
direc =-1
for char in text:
    ans[i]+=char
    if(i==0 or i==row-1):
        direc*=-1
    i+=direc
print(''.join(ans))
       
    