# გააკეთეთ Reverse List და გამოიყენეთ while loop. შემოაბრუნეთ ყველა რიცხვი ლისტში

my_list = []

i = 0

while i < 5:
    num = input("Enter Num:")
    my_list.append(num)
    i = i + 1

my_list.reverse()
print(my_list)
