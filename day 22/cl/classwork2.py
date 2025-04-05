num = int(input("enter number: "))

sum = 0

sum2 = 0

for i in range(num):
    if i % 2 == 0:
        sum += i
    if i % 2 != 0:
        sum2 += i


print(sum)
print(sum2)