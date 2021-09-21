n=int(input())
m=n
rev=0
while n>0 :
    rev=(rev*10)+(n%10)
    n=n//10
if (rev==m) :
    print("Palindrome")
else :
    print("Not Palidrome")