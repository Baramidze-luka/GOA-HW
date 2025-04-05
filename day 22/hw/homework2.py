# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის კვადრატის ჯამი

num = int(input("Enter Num:"))

sum = 0
for i in range(num):
    i = i * i
    sum = (sum + i) 

print(sum)
