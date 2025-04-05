


my_list = [23,25,75,22,5,11,83,90,54,88]

for i in range(len(my_list)):
    if my_list[i] % 5 == 0:
        print(str(my_list[i]) + " 5-ზე იყოფა")
    elif my_list[i] % 3 == 0:
        print(str(my_list[i]) + " 3-ზე იყოფა")