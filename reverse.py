n1=int(input("enter a number"))
rev=0
while n1>0:
    rem=n1%10
    print(rem)
    rev=(rev*10)+rem
    print(rev)
    n1=n1//10
    print(n1)
print(rev)