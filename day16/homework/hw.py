# cw1
num = float(input("enter a number: "))
if num>0:
    print("ეს რიცხვი დადებითია")
elif num<0:
    print("ეს რიცხვი უარყოფითია")
else:
    print("ეს რიცხვი ნულია")

# cw2
age = int(input("enter your age: "))
if 0<=age<=12:
    print("ბავშვი ხარ")
elif 13<=age<=19:
    print("მოზარდი/თინეიჯერი ხარ")
elif 20<=age<=64:
    print("ზრდასრული ხარ")
elif 65<=age<=120:
    print("ხანში შესული ხარ")
elif 120<age:
    print("გურუ ან ჯადოქარი")
else:
    print("არასწორი ინფო")

# cw3
#password guesser
password = "mchagvreli123"

tries = 3

while tries>0:
    password_1=input("enter your password")
    if password_1==password:
        print("პაროლი სწორია")
        break
    else:
        tries = tries - 1
        if tries>0:
            print("try again")
        else:
            print("nah strong password")

# cw4
num1 = ""
num2 = ""
num3 = ""
num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
num3 = float(input("enter your third number: "))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

# cw5
print("კვირის დღეები")
print("1. ორშაბათი")
print("2. სამშაბათი")
print("3. ოთხშაბათი")
print("4. ხუთშაბათი")
print("5. პარასკევი")
print("6. შაბათი")
print("7. კვირა")

choice = int(input("აირჩიეთ კვირის დღე (1-7): "))
if choice == 1:
    print("ორშაბათი")
elif choice == 2:
    print("სამშაბათი")
elif choice == 3:
    print("ოთხშაბათი")
elif choice == 4:
    print("ხუთშაბათი")
elif choice == 5:
    print("პარასკევი")
elif choice == 6:
    print("შაბათი")
elif choice == 7:
    print("კვირა")
else:
    print("ეგეთი დღე არ ვიცი მე")