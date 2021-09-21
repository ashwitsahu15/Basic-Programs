s=input()
vow=0
con=0
for i in s :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' :
        vow+=1
    else :
        con+=1
print(vow,con)