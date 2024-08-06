def direc():
    count_N=size[1]
    count_S=size[1]
    count_W=size[0]
    count_E=size[0]
    
    
    ans=[]
    for i in range(1,x):
            for j in range (y):
                if lis_n[i][j]>lis_n[0][j]:
                    count_N+=1
                    lis_n[0][j]=lis_n[i][j]

    for i in range(x-2,0,-1):
            for j in range (y):
                if lis_s[i][j]>lis_s[x-1][j]:
                    count_S+=1
                    lis_s[x-1][j]=lis_s[i][j]

    for i in range(x):
            for j in range(y-2,0,-1):
                if lis_e[i][j]>lis_e[i][y-1]:
                
                    count_E+=1
                    lis_e[i][y-1]=lis_e[i][j]

    for i in range(x):
            for j in range (1,y):
                if lis_w[i][j]>lis_w[i][0]:
                    
                    count_W+=1
                    lis_w[i][0]=lis_w[i][j]

    ans=[count_N,count_S,count_E,count_W]
    #print (ans)
    maxx=max(ans)
    temp=[]
    for i in range(len(ans)):
         if ans[i]>=maxx:
              if(i==0):
                   temp.append('N')
              elif i==1:
                   temp.append('S')
              elif i==2:
                   temp.append('E')
              elif i==3:
                   temp.append('W')
    
    return temp




size = list(map(int,input("City Size: ").split()))
x=size[0]
y=size[1]

lis=[]
for i in range(x):
    n=list(input().split())
    lis.append(n)

lis_n = [row[:] for row in lis]
lis_s = [row[:] for row in lis]
lis_w = [row[:] for row in lis]
lis_e = [row[:] for row in lis]


final = direc()
print(" ".join(final))
