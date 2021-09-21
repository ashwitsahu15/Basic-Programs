n=int(input())
prime=[True for x in range(n+1)]
p=2
while(p*p)<=n :
    if prime[p] :
        for i in range(p*p,n+1,p) :
            prime[i]=False
    p+=1
for i in range(n+1) :
    if prime[i] and i>1:
        print(i)