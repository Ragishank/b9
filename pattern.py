# limit=int(input("enter the limit"))
# str1=""
# for i in range(0,limit):
#     for x in range(0,i+1):
#         str1=str1+"*"
#         print(str1)
#     print("\n")
num=int(input("enter the limit"))
for i in range(num):
    for j in range((num - i) - 1):
        print(end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()