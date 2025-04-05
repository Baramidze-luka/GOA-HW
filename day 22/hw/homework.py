#  მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი
num = int(input("Enter Num:"))

sum = 0
for i in range(num):
    sum = sum + i
    
print(sum)