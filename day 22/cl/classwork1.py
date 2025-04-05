num = int(input("enter number: "))

sum = 0

for i in range(num):
    if i % 2 == 0:
        sum += i

print(sum)