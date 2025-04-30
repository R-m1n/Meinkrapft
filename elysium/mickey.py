def fib(n):
    a, b = 0, 1
    for _ in range(n + 1):
        a, b = a + b, a

    return a

import math
import turtle



def draw_triangle(t: turtle, size: float = 0):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_square(t: turtle, size: float = 0):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_lozi(t: turtle, size: float = 0):
    angles = [120, 60, 120, 60]
    for i in range(4):
        t.left(angles[i])
        t.forward(size)

def draw_pentagon(t: turtle, size: float = 0):
    for _ in range(5):
        t.forward(size)
        t.left(72)

def draw_hexagon(t: turtle, size: float = 0):
    for _ in range(6):
        t.forward(size)
        t.left(60)

def draw_octagon(t: turtle, size: float = 0):
    for _ in range(8):
        t.forward(size)
        t.left(60)

def draw_circle(t: turtle, size: float = 0):
    for _ in range(400):
        t.forward(size / 10)
        t.left(1)

def draw_semi_circle(t: turtle, size: float = 0):
    for _ in range(200):
        t.forward(size / 10)
        t.left(1)

def mitsubishi_spiral(t: turtle):
    colors = ['white', 'orange']
    size = 10

    for epoch in range(400):
        color = colors[epoch % len(colors)]

        if epoch % 2 == 0:
            t.pencolor(color)
            draw_lozi(t, (epoch + size) / 1.5)
            t.left(15)

        elif epoch % 3 == 0:
            t.pencolor('white')
            t.fillcolor(color)
            t.begin_fill()
            draw_lozi(t, (epoch + size) / 2)
            t.end_fill()
            t.left(72)

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=1.0, height=1.0)

t = turtle.Turtle()
t.pensize(1.5)
t.speed(0)
colors = ['white', 'orange', 'yellow', 'blue', 'red', 'violet']
colors = ['white', 'orange']
colors = ['#E4ACB2', '#B83453', '#CF5C75']
screen.tracer(8, 25)

size = 0

for epoch in range(50):
    color = colors[epoch % len(colors)]

    t.pencolor(color)
    t.left(30)
    draw_semi_circle(t, (epoch + size) / 1.5)

t.left(30)
draw_semi_circle(t, (epoch + size) / 1.5)

screen.exitonclick()