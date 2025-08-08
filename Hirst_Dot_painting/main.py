# import colorgram
# colors=colorgram.extract("Screenshot 2025-04-05 145718.png",30)
# list=[]
# for color in colors:
#     r= color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     list.append((r,g,b))
#
# print(list)
import random
import turtle

from turtle import Turtle,Screen
screen=Screen()
tim=Turtle()
turtle.colormode(255)
tim.penup()       # Prevent drawing a line while moving
tim.goto(-200,-100)
tim.pendown()

p=-100
color_list=[(233, 227, 84), (233, 53, 130), (200, 78, 15), (107, 181, 215), (199, 8, 67), (195, 162, 13), (219, 160, 99), (31, 103, 166), (212, 134, 173), (231, 225, 7), (35, 191, 110), (15, 26, 69), (23, 28, 162), (233, 166, 195), (15, 182, 210), (199, 33, 126), (128, 187, 159), (12, 48, 30), (57, 15, 29), (47, 127, 81), (236, 67, 36), (112, 91, 209), (130, 217, 232), (150, 216, 197), (185, 17, 8), (10, 96, 58)]
for i in range(10):
    tim.penup()
    tim.goto(-200,p)
    tim.pendown()

    for j in range(10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    p+=50

screen.exitonclick()




