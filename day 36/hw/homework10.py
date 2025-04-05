num = int(input("Enter Num:"))

def number(num):
    i = 1
    while i != num + 1:
        if i % 2 == 1:
            print(i)
        i+= 1

number(num)