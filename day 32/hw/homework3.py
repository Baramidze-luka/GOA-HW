#  გააკეთეთ Find Minimum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მინიმალური ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [1]

my_list = [1, 546, 456, 123]

num = my_list[0]

for i in my_list:
    if i < num:
        num = i
        
print(num)