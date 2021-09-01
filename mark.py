mark=[]
total=0
for i in range(5):
    a=int(input("enter your mark"))
    mark.append(a)
for i in mark:
    total=total+i
print(total)
if(total>90):
    print("A grade")
elif(total>80):
    print("b Grage")
elif(total>70):
    print("c Grage")
else:
    print("your failed")