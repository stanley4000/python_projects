#Task: use turtle graphics to simulate Damion Hirst spot paintings

import random
import turtle

# color_list = []
# colors = cg.extract("hirst.jpg", 100)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)
#

color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]


t = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.colormode(255)


# #NOte: built-in function dot()
# def draw_spot():
#     # draws a filled circle radius 10, color randomly selected from list
#     ran_color = random.choice(color_list)
#     t.pencolor(ran_color)
#     t.fillcolor(ran_color)
#     t.pendown()
#     t.begin_fill()
#     t.circle(10)
#     t.end_fill()
#     t.penup()


t.speed("fastest")
t.penup()
t.hideturtle()
x_pos = -225
y_pos = -220
t.setx(x_pos)
t.sety(y_pos)
t.setheading(0)

def create_row():
    # uses dot() to create a row of spots
    for dots in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)


i = 1
while i <= 10:
    create_row()
    t.setx(x_pos)
    y_pos += 50
    t.sety(y_pos)
    i += 1



# while t.ycor() >= -my_screen.canvheight / 2 :
#     create_row()

my_screen.exitonclick()
