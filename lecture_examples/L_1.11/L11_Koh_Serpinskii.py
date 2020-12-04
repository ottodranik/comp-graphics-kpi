# --------------- ПРИКЛАД: фрактал КОХА (сніжинка), фрактал Серпінського (трикутник) ------
import turtle
from random import random, randrange
# --------------- однократний фрактал КОХА (сніжинка), ------------------------------------
size = 300; n = 2;
def koch_curve(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)

def draw_koch_snowflake(size, n):
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)

draw_koch_snowflake(size, n)
# --------------- багатократний фрактал КОХА (сніжинка) - як форма черепашки ---------
def koch_curve(turtle, steps, length):
    if steps == 0:
        turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, steps - 1, length / 3)
            turtle.left(angle)

def koch_snowflake(turtle, steps, length):
    turtle.begin_poly()

    for _ in range(3):
        koch_curve(turtle, steps, length)
        turtle.right(120)

    turtle.end_poly()

    return turtle.get_poly()
# ------------------------------ зміна характеристик черепахи ---------------------
turtle.speed("fastest")
turtle.register_shape("snowflake", koch_snowflake(turtle.getturtle(), 3, 100))
turtle.reset()
turtle.penup()
turtle.shape("snowflake")

width, height = turtle.window_width() / 2, turtle.window_height() / 2
width=int(width)
height =int(height)
for _ in range(24):
    turtle.color((random(), random(), random()), (random(), random(), random()))
    turtle.goto(randrange(-width, width), randrange(-height, height))
    turtle.stamp()

# ------------------------------ зміна характеристик черепахи ---------------------
turtle.shape("square")
turtle.stamp()
turtle.forward(1)
# ---------------  фрактал Серпінського (трикутник) --------------------------------

turtle.Turtle().ht()
turtle.speed(10)
turtle.pencolor('blue')

turtle.speed(0)
points = [[-175,-125],[0,175],[175,-125]]

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def triangle(points,depth):

    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()
    turtle.goto(points[1][0],points[1][1])
    turtle.goto(points[2][0],points[2][1])
    turtle.goto(points[0][0],points[0][1])

    if depth>0:
        triangle([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   depth-1)
        triangle([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   depth-1)
        triangle([points[2],
                         getMid(points[2], points[1]),
                         getMid(points[0], points[2])],
                   depth-1)


triangle(points,4)
turtle.done()
# ---------------------------------------------------------------------------------