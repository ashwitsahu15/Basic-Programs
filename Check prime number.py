def prime(n) :
    if n<=1 :
        return False
    for i in range(2,n) :
        if n%i==0 :
            return False
    return True
# shortcut :
import math
def isprime(n) :
    if n==1 :
        return False
    if n==2 or n==3 :
        return True
    if n%2==0 or n%3==0 :
        return False
    for i in range(5,int(math.sqrt(n))+1,5) :
        if n%i==0 or n%(i+2)==0 :
            return False
    return True
