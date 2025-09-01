# cw 1
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
num3 = int(input('enter your thirds number: '))

if num1==num2:
    print("პირველი და მეორე რიცხვი ტოლია")
elif num1==num3:
    print("პირველი და მესამე რიცხვი ტოლია")
elif num2==num3:
    print("მეორე და მესამე რიცხვი ტოლია")
elif num1==num2==num3:
    print("სამივე რიცხვი ტოლია")
else:
    print("არცერთი რიცხვი არ არის ტოლი")

# cw 2
num = int(input("enter a number(1-12): "))
if num==1 or num==12 or num==2:
    print("ზამთარი")
elif num==3 or num==4 or num==5:
    print("გაზაფხული")
elif num==6 or num==7 or num==8:
    print("ზაფხული")
elif num==9 or num==10 or num==11:
    print("შემოდგომა")
else:
    print('invalid choice')

name = input("enter your name: ")
if name=="admin":
    password = input("enter your password: ")
    if password=="adminpassword123":
        print('სალამი ადმინ')
    else:
        print("წვდომა არ არის")
else:
    print("სალამი სხვა მომხმარებელს")