#  მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ნამრავლი


num = int(input("Enter Num:"))

sum = 1

for i in range(1,num):

    sum = sum * i

print(sum)