a=[20,30,44]
total=a[0]+a[2]+a[1]
print(total) 
if total > 85 and total <= 100:  
   print("Congrats ! you scored grade A ...")  
elif total > 60 and total <= 85:  
   print("You scored grade B + ...")  
elif total > 40 and total <= 60:  
   print("You scored grade B ...")  
elif (total > 30 and total <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail ") 
