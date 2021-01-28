from turtle import Turtle, Screen
import random
import turtle

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


turtle.colormode(255)
painter = Turtle()
painter.shape('arrow')
no_of_circles = 36
angle = 0
increment = 360/no_of_circles
for i in range(no_of_circles):
    painter.color(get_random_color())
    painter.setheading(angle)
    painter.circle(100)
    angle += increment

screen = Screen()
screen.exitonclick()
