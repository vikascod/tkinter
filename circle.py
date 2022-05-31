import turtle

star = turtle.Turtle()
star.color("green")
star.forward(100)

a = turtle.Screen()
a.bgcolor("yellow")

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()