str1 = input("enter a string")
countDict = dict()
for i in str1:
  count = str1.count(i)
  countDict[i]=count
print(countDict)