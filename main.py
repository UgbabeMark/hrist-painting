import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(229, 227, 224), (227, 223, 225), (217, 226, 220), (195, 172, 122), (221, 226, 232), (159, 100, 58),
              (186, 161, 51), (126, 37, 25), (8, 54, 78), (52, 34, 29), (109, 70, 85),
              (118, 162, 175), (26, 119, 167), (74, 35, 43), (86, 139, 65),
              (9, 64, 44), (69, 153, 133), (121, 35, 40), (182, 98, 82),
              (209, 202, 146), (146, 177, 160), (176, 148, 154), (176, 203, 188),
              (218, 179, 172), (30, 79, 61), (23, 77, 92), (93, 143, 149),
              (159, 108, 112), (218, 179, 183), (168, 202, 208)]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()