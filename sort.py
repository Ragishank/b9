print("How many number:")
k = int(input())

list1 = []
print("Enter numbers:")

for i in range(0, k):
    num = int(input())

    list1.append(num)

print("Number before sorting:", list1)



for i in range(0, len(list1)):
    for j in range(1 + i, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print("After Sorting numbers are:", list1)