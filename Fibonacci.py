num = int(input("Enter the number of fibonacci numbers :"))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    sum = a+b
    print(sum)
    a = b
    b = sum