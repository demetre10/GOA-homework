from turtle import *


#we want to paint a hoese

#step 1: draw a square

speed(30)
width(7)
color("orange")
begin_fill()
 
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("brown")
begin_fill()
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

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
left(130)

penup()
goto(200,120)
pendown()
color("blue")
begin_fill()
left(170)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


color("blue")
penup()
goto(200,200)
right(90)
forward(200)
pendown()
left(90)
penup()
forward(30)
pendown()
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()







exitonclick()