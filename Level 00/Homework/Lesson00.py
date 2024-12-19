from turtle import *
color("yellow")
# drawing a squere
width(7)
speed(10)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
# drawing a door

left(90)

forward(70)
color("green")
left(90)
forward(85)
right(90)
forward(42.5)
right(90)
forward(85)
# drawing a roof
penup()
goto(200, 200)
pendown()
color("blue")

right(150)
forward(200)
left(120)
forward(200)

# drawing a windws
penup()
goto(15,130)
pendown()
color("purple")
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)


penup()
goto(185,130)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

exitonclick()