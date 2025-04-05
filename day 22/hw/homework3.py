# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ორზე ნამრავლების ჯამი

num = int(input("Enter Num:"))

sum = 0
for i in range(num):
    i = i * 2
    sum = (sum + i) 

print(sum)