st1=input("enter astring")
st2=input("enter a string")
l1=len(st1)
l2=len(st2)
st_new=st1[0]+st2[0]+st1[l1//2]+st2[l2//2]+st1[l1-1]+st2[l2-1]
print(st_new)