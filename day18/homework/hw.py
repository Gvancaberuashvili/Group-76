# hw1
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

if num1>num2:
    print("first number is more than second")
elif num1<num2:
    print("first number is less than second")
else:
    print("first number is equal to second")

# hw2
my_name = "gvanca"
name = input("enter your name: ")
if my_name==name:
    print("სეხნიები ვართ")
else:
    print("სხვადასხვა სახელები გვაქვს")

# hw3
num3 = int(input("enter your first number: "))
num4 = int(input("enter your second number: "))

if num3>0 and num4>0:
    print("ორივე რიცხვი დადებითია")
elif num3<0 and num4<0:
    print("ორივე რიცხვი უარყოფითია")
else:
    print("ეს რა ჯანდაბაა")

# hw4
for i in range(50,100,2):
    print(i)

# hw5
i = 20
while i<40:
    print(i)
    i = i + 1

