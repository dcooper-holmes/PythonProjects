import turtle as t
import random
import colorgram

# -- Colorgram Code to extract colors from 'hirst-painting.jpg' image --
# rgb_colors = []
# colors = colorgram.extract('hirst-painting.jpg', 10)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

t.colormode(255)
timmy = t.Turtle()
screen = t.Screen()

timmy.penup()
timmy.speed(0)
timmy.hideturtle()

new_colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156)]

screen_size = screen.screensize()

starting_point_x = -screen_size[0]
starting_point_y = -screen_size[1]

timmy.teleport(starting_point_x, starting_point_y)

while timmy.position() != screen_size:
    
    if timmy.position()[0] != screen_size[0]:
        timmy.dot(20, (random.choice(new_colors)))
        timmy.forward(50)
    else:
        starting_point_y += 50
        timmy.teleport(starting_point_x, starting_point_y)

screen.exitonclick()