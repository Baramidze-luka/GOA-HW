# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ რიცხვების საშუალო არითმეტიკული


num = int(input("Enter Num:"))

sum = 0

for i in range(num):
    sum = (sum + i)
print(sum / num)