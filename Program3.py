a = int(input("Enter a number: "))
result = []
count = (a + 1) // 2    # Only odd positions count
num = 1
for i in range(count):
    result.append(num)
    num += 2
print(*result, sep=", ")