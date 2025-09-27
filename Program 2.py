a = int(input("Enter a number: "))
result = []
num = 1
for i in range(a):
    result.append(num)
    num += 2
print(*result, sep=", ")