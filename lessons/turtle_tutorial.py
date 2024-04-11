"""Introduction to Turtle."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.speed(5)
leo.hideturtle()

leo.color(147, 22, 150)
leo.fillcolor("red")
leo.penup()
leo.goto(-50, -50)
leo.pendown()
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(200)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.goto(-50, -50)
bob.speed(100)
i: int = 0
while (i < 3):
    bob.forward(200)
    bob.left(120)
    i = i + 1

side_length: int = 300
i: int = 0
while (i < 150):
    bob.forward(side_length)
    bob.left(120.5)
    i = i + 1
    side_length = side_length * 0.96

done()