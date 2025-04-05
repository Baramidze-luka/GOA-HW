num = [56,35, 23,54,65,123,6752,2342756,234,7645]

sum_num = []

for i in range(len(num)):
    if num[i] % 2 == 0:
        sum_num += [num[i]]

print(sum_num)