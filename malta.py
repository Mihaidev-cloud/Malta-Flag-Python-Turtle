from turtle import *
import turtle
import os
import tkinter

speed(2)
setup(800,500)
turtle.title("Malta Flag Python")

root = turtle.Screen()._root
root.iconbitmap("malta_flag.ico")

penup()
goto(-10, 250)
pendown()

#red
color("red")
width(1)
begin_fill()
forward(400)
right(90)
forward(490)
right(90)
forward(400)
right(90)
forward(400)
right(90)
end_fill()


#cross


turtle.up()
turtle.goto(-380,130)
turtle.down()
width(3)
turtle.fillcolor("grey")
turtle.begin_fill()
for _ in range(4):
    turtle.fd(50)
    turtle.right(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)      
turtle.end_fill()

turtle.exitonclick()
