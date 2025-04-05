#  გააკეთეთ Sum Of Odd Numbers. მიზანი: შეკრიბეთ ყველა კენტი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = []

for i in num:
    if i % 2 == 1: 
        even_num.append(i)  

sum_of_even_numbers = sum(even_num)

for _ in range(10):
    print(sum_of_even_numbers)
