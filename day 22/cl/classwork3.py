num = int(input("enter your nmber:" ))

sum = 0
sum2 = 0

i = 0

while i < num:
    if i % 5 == 0:
        sum += i
    elif i % 3 == 0:
        sum2 += i
    i += 1

print(sum)
print(sum2)