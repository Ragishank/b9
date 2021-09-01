limit=int(input("enter your limit"))
a=0
b=1
c=0
print(a)
print(b)
for i in range(2,limit):
    c=a+b
    print(c)
    a=b
    b=c

