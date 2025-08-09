#1
num1 = (int(input("enter your first number: ")))
num2 = (int(input("enter your second number: ")))

print(num1 < num2)
print(num1 > num2)
print(num1 == num2)

#2
num3 = "10"
num4 = "20"
num5 = "30"
num6 = 40
num7 = 50

print(((int(num3)) + (int(num4)) + (int(num5)) + num6 + num7) / 5)

#3
name = (input("enter your name: "))
surname = (input("enter your surname: "))
country = (input("enter where you are from: "))
number = (int(input("enter a number: ")))

print((name + surname + country) * number)

#4
#ვისწავლეთ ორი ლოგიკური ოპერატორი "and" და "or" ოპერატორები
# "and" ოპერატორის გამოყენების დროს თუ ერთი პირობა არის False, მაშინ ყველა პირობა არის False.
# "or" ოპერატორის გამოყენების დროს თუ ერთი პირობა არის True, მაშინ ყველა პირობა არის True.

#5
# (and)                             (or)
# True and True --  True     |   True or True -- True          
# True and False -- False     |   True or False -- True
# False and True -- False  |   False or True -- True
# False and False -- False    |   False or False -- False

#6
# "and" ოპერატორის მაგალითები:
print(5>10 and 5<10)
print(5<10 and 5==10)

# "or" ოპერატორის მაგალითები
print(5>10 or 5<10)
print(5<10 or 5==10)

#7
show = "game og thrones"
episodes = 73
duration = 59.60
best_show = True

print(type(show))
print(type(episodes))
print(type(duration))
print(type(best_show))

#8
print(input("what is your favourite show: "))
print(int(input("how many episodes does it have?: ")))
print(float(input("what is the average duration of one episode? ")))
