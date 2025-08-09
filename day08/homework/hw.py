#1
print(10<5 and 4<8)
print(10>20 and 100<50)
print(14==15 and 16>5)
print(700>500 and 45<3)
print(300==500 and 67<89)
print(20>5 or 16<40)
print(300<700 or 40==8)
print(25==25 or 50==50)
print(1>0 or 1<0)
print(150==150 or 300<30)

#2
#sequancing -- თანმიმდევრობა, 

#iteration - რაღაც მნიშვნელობის გამოეორება რამდენჯერმე ან უსასრულოდ. 

#selection - არჩევანი მნიშვნელობებს შორის. 

#3
#sequencing მაგალითი არის კოდის წაკითხვა, რომელიც ხდება თანმიმდევრობით ზემოდან ქვემოთ.
print("cave")
print("rock")
print("table")

#4
#loop- კონკრეტული მნიშვნელობის რამდენჯერმე ან უსასრლოდ გამეორება, რომელიც გვეხმარება ერთი და იგივე მნიშნელობა ტერმინალზე
#უფრო მარტივად და ნაკლები შრომის გარეშე გამოვიტანოთ.

#5
# range() ფუნქციას გადაეცემა ის რიცხვი რამდენჯერაც გვინდა რომ ჩვენი კონკრეტული მნიშვნელობა აისახოს ტერმინალზე.

#6
for i in range(100):
    print("beruashvili")

#7
for i in range(40):
    print("green")

#8
for i in range(32):
    print("G")

#9
name = (input("enter your name: "))
surname = (input("enter your surname: "))
country = (input("enter which country are you from: "))
age = (int(input("enter your age: ")))

print(name + surname + country + str(age)) 

#10
city = "london"
score = 80
height = 1.75
winner = True

print(type(city))
print(type(score))
print(type(height))
print(type(winner))

#11
num1 = (int(input("enter your first number: ")))
num2 = (int(input("enter your second number: ")))
num3 = (int(input("enter your third number: ")))
num4 = (int(input("enter your fourth number: ")))

print(num1 + num2 + num3 + num4)
