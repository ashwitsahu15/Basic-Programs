s=input()
print(s[::-1])
s=list(s)
n=len(s)
for i in range(n//2) :
    print(i,n)
    (s[i],s[n-1])=(s[n-1],s[i])
    n-=1
print(*s,sep='')
print("HELLO WORLD")
