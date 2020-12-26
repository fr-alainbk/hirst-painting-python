import colorgram
import turtle as t
import random

leo = t.Turtle()
t.colormode(255)
leo.pensize(1)
leo.speed("normal")
leo.setheading(225)
leo.hideturtle()
leo.penup()
leo.forward(250)
leo.setheading(0)

color_list = [(230, 207, 91), (225, 149, 91),
              (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145), (233, 81, 49), (202, 67, 27),
              (192, 186, 23), (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39), (12, 41, 76), (242, 203, 4),
              (139, 79, 92), (88, 13, 20), (53, 166, 76), (51, 23, 19), (180, 134, 146), (6, 64, 137), (213, 68, 75),
              (230, 170, 161), (49, 151, 191), (77, 133, 186), (175, 204, 176)]


def draw_painting(space):
    for _ in range(10):
        for _ in range(10):
            leo.dot(20, random.choice(color_list))
            leo.forward(space)
        leo.right(180)
        leo.forward(space * 10)
        leo.right(90)
        leo.forward(space)
        leo.right(90)


draw_painting(50)




# colors = colorgram.extract('painting.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)






screen = t.Screen()
screen.exitonclick()