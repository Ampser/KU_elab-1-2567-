text = list(map(str,input("Text: ").split()))
lenge=0
maxx=0
chain=1
temp=0
for i in range (len(text)-1):
    for j in range(len(text[i])):
        if text[i][j]!=text[i+1][j]:
            temp+=1
    if temp>2:
            chain+=1
            lenge=0
    else:
        lenge+=1
    if lenge>maxx:maxx=lenge
        
        
    temp=0
print(f"{chain} Chain(s). Maximum length is {maxx+1} word(s).")    
        