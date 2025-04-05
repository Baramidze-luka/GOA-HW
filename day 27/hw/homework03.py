num = list(range(1, 31))

while True:
    user_num = int(input("enter number: "))
    if user_num == 5:
        print("You guessed the number!")
        break
    elif user_num > 30:
        print("Incorrect, Please try again")
    else:
        print("You must enter a number from 1 to 30")
        continue