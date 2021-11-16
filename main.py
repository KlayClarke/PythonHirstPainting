from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed('fastest')

color_list = [(199, 175, 117), (212, 222, 215), (125, 36, 24), (167, 106, 56),
              (186, 159, 52), (6, 57, 83), (108, 68, 85)]


def create_line(number_of_spots_per):
    for _ in range(number_of_spots_per):
        r = random.choice(color_list)
        tim.dot(20, r)
        tim.forward(50)


def next_line(number_of_spots_per):
    for _ in range(number_of_spots_per):
        tim.backward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)


def create_art(number_of_rows, number_of_spots_per):
    for _ in range(number_of_rows):
        create_line(number_of_spots_per)
        next_line(number_of_spots_per)


create_art(5, 5)

my_screen = Screen()
my_screen.exitonclick()
