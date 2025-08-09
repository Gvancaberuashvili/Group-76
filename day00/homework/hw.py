from turtle import *

#building a house

#step 1: draw a square
speed(30)
width(7)
color("blue")
forward (200)
left (90)

forward (200)
left(90)

forward (200)
left (90)

forward (200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("pink")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("black")

left(30)
forward(70)
left(90)
forward(65)
left(90)
forward(70)
left(90)
forward(65)

penup()
goto(200, 200)
pendown()
forward(70)
left(90)
forward(65)
left(90)
forward(70)
left(90)
forward(65)

exitonclick()