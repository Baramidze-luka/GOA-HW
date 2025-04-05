# შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.


num = (input("Enter Number"))
num2 = (input("Enter NUmber:"))

if num > "10":
    print(num + "მეტია 10-ზე")
elif num < "10":
    print(num + "ნაკლებია 10-ზე")


if num2 < "50":
    print(num2 + "ნაკლებია 50-ზე")
elif num2 > "50":
    print(num2 + "მეტია 50-ზე")