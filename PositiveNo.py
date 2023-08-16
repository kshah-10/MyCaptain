list = []
lst = []
n = int(input("Enter the number of integers :"))
for i in range(0,n):
    x = int(input())
    list.append(x)
print(list)
for i in list:
    if i>=0:
        lst.append(i)
print(lst)