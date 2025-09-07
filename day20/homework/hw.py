# hw1
# +
print(5 + 9)
print(6 + 10)
print(3 + 7)

# - 
print(15 - 5)
print(4 - 6)
print(67 - 10)

# *
print(3 * 9)
print(7 * 8)
print(123 * 56)

# /
print(14 / 7)
print(45 / 7)
print(135 / 5)

# //
print(10 // 3)
print(10 // 7)
print(20 // 6)

# **
print(2 ** 2)
print(3 ** 4)
print(7 ** 2)

# %
print(10 % 6)
print(20 % 10)
print(150 % 35)

# hw2
#ვისწავლეთ სამი ახალი მათემატიკური ოპერაცია, ესენია: // , ** , % .
# // - გაყოფა , რომელიც გვეუბნება გასაყოფი რამდენჯერ მოთავსდება გამყოფში და გამოაქვს მხოლოდ ინტეჯერ ტიპის მონაცემი.
# ** - ხარისხებში გამრავლება, რომელიც გასამრვავბლებელ რიცხვს თავის თავზე კონკრეტული რაოდენობით გაამრავლებს.
# % - პროცენტული იგივე ნაშთიანი გაყოფა, რომელსაც გამოაქვს ტერმინალში ნაშთი.

# hw3
# //
print(10 // 3)
print(10 // 7)
print(20 // 6)
print(30 // 7)
print(60 // 5)

# **
print(2 ** 2)
print(3 ** 4)
print(7 ** 2)
print(4 ** 3)
print(3 ** 2)

# %
print(10 % 6)
print(20 % 10)
print(150 % 35)
print(130 % 45)
print(60 % 45)

# hw4
#      15 / 3 =5 
#      20 / 4 = 5
#      100 / 20 = 5

#      15 // 10 = 1
#      10 // 7 = 1
#      40 // 12 = 3

#      4 * 3 = 12
#      40 * 3 = 120
#      120 * 3 = 360

#      4 ** 3 = 64
#      10 ** 3 = 1000
#      2 ** 6 = 64
#      3 ** 4 = 81

#      10 % 7 = 3
#      3 % 2 = 1
#      50 % 25 = 0
#      14 % 11 = 3
#      110 % 50 = 10

# hw5
#სიები იმით განსხვავდება ცვლადებისგან, რომ სიებში შეგვიძლია რამდენიმე და ასსევე განსხვავებული ტიპის მონაცემები შევინახოთ, ხოლო ცვლადში მხოლოდ 
#ერთი მონაცემის შენახვაა შესაძლებელეი. სიებს ვიყენებთ ბევრი მონაცემის შესანახად.

# hw6-7-8-9-10
string_list = ["bondo","manana","lela","nunu","esma"]
int_list = [12,34,54,67,8]
float_list = [12.4,3.5,4.5,17.3]
boolean_list = [True,False]
all_list = ["bondo",12,34.5,True]

# hw11
num1=int(input("enter your first number: "))
num2=int(input("enter your second number: "))
print(num1 // num2)
print(num1 ** num2)
print(num1 % num2)

# hw12
num=int(input("enter your number: "))
if 30<num<100:
    print("between 30 and 100")
elif 100<num<200:
    print("between 100 and 200")
else:
    print("other number")

# hw13
var1="manana"
var2=20
var3=4.5
var4=True
var5="lile"

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

# hw14
i=50

while i < 100:
    print(i)
    i=i+3

# hw15
for i in range(40,90,3):
    print(i)

# hw16
for i in range(15):
    print("gvanca beruashvili")

i=0
while i > 15:
    print("gavnca beruashvili")

# hw17
my_name="gvanca"
my_surname="beruashvili"
name=input("enter your name: ")
surname=input("enter your surname: ")

if my_name==name and my_surname==surname:
    print("ame name and surname")
elif my_name==name and my_surname!=surname:
    print("same name but different surname")
else:
    print("aqedan moshordi")

# hw18
password="goga"
password1=input("enter your password: ")

while True:
    if password==password1:
        print("gamoicani")
        break
    else:
        print("try again")