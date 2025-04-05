# შექმენით shopping სია სადაც მომხმარებელს შეეძლება რამე ნებისმიერი პროუქტის დამატება და წაშლა, როდესაც მორჩებიან შოპინგს დაუპრინტეთ საბოლოოდ რა შეიძინეს 


add_item = input("Enter Item:")

shop = []

shop.append(add_item)
print(shop)

delete_item = input("Enter Item To Delete:")

shop.remove(delete_item)

print(shop)