# count=0
# limit=int(input("enter your limit"))
# while count<limit:
#     print (count)
#     count=count+1
    
password="cybersqure"
guess=""
while password != guess:
    guess=input("enter the password")
    if password==guess:
        print("login success")
    else : print("login failed")