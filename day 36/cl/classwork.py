num1 = int(input("Enter Num:"))
num2 = int(input("Enter Num1:"))

def namravli(num1,num2):
    num = num1 * num2
    if num % 2 == 0:
        print(str(num) + " Luwia")
    else:
        print(str(num) + " Kentia")

namravli(num1,num2)
    