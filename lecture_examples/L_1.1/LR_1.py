#-------------------------------------3D-1---------------------------------------
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy

# def makeData ():
#     x = numpy.arange (-10, 10, 0.1)
#     y = numpy.arange (-10, 10, 0.1)
#     xgrid, ygrid = numpy.meshgrid(x, y)

#     zgrid = numpy.sin (xgrid) * numpy.sin (ygrid) / (xgrid * ygrid)
#     return xgrid, ygrid, zgrid

# x, y, z = makeData()

# fig = pylab.figure()
# axes = Axes3D(fig)

# axes.plot_surface(x, y, z)

# pylab.show()

#-------------------------------------3D-2---------------------------------------

import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
import numpy

# def makeData ():
#     x = numpy.arange (-10, 10, 0.1)
#     y = numpy.arange (-10, 10, 0.1)
#     xgrid, ygrid = numpy.meshgrid(x, y)

#     zgrid = numpy.sin (xgrid) * numpy.sin (ygrid) / (xgrid * ygrid)
#     return xgrid, ygrid, zgrid

# x, y, z = makeData()

# fig = pylab.figure()
# axes = Axes3D(fig)

# axes.plot_surface(x, y, z, rstride=4, cstride=4, cmap = cm.jet)

# pylab.show()

#----------------------------------------------------------------------------------------------
print("****************************************************************************************")
print("---------------------димонстарція графічних можливостей python--------------------------")
print()
print('-1-----------------димонстарція графічних можливостей модуля tkinter--------------------')
from tkinter import *

window = Tk()
window.title('Работа с canvas - абстракція tkinter')

canvas = Canvas(window,width=600,height=600,bg="gray",
          cursor="pencil")

canvas.create_polygon([400,400],[300,400],[350,300],fill="gray", outline="yellow")
canvas.create_rectangle(50,250,300,500,fill="white",outline="blue")
canvas.create_oval([400,250],[450,300],fill="pink")
canvas.create_line(0,0,600,600,width=5,fill="yellow")

canvas.pack()
window.mainloop()

print('-------------------------------ВІТАЮ, зображення сформовано----------------------------')

print(" ")
print("****************************************************************************************")
print('-2------димонстарція графічних можливостей модуля наукової графіки matplotlib-----------')
print('-----------------------малюємо графік лінійної функції----------------------------------')

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()

print('-малюємо три діагональні кола в координатній сітці вікна та записуемо результат у файл--')

circle1 = plt.Circle((0, 0), 0.2, color='r')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)

fig, ax = plt.subplots()

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

fig.savefig('plotcircles1.png')
print('-----------------------------ВІТАЮ, перший файл сформовано------------------------------')
print('-----малюємо два великіх кола по діагональним кутам та маленькі в середині--------------')
circle1 = plt.Circle((0, 0), 2, color='r')
circle2 = plt.Circle((5, 5), 0.5, color='b', fill=False)
circle3 = plt.Circle((10, 10), 2, color='g', clip_on=False)

ax = plt.gca()
ax.cla()
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

ax.plot(range(11), 'o', color='black')
ax.plot((5), (5), 'o', color='y')

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
fig.savefig('plotcircles2.png')

print('-------------------------------ВІТАЮ, другий файл сформовано----------------------------')
print("****************************************************************************************")
print(" ")
print('-3-----------димонстарція можливостей черепахової графіки модуль turtle-----------------')
print('------------------------малюємо динамічну побудову кола---------------------------------')

import turtle
import math

a = 150
b = 90
dx = turtle.xcor()
dy = turtle.ycor()
for deg in range(361):
    rad = math.radians(deg)
    x = a * math.sin(rad) + dx
    y = -b * math.cos(rad) + b + dy
    turtle.goto(x, y)
print('-------------------------------ВІТАЮ, коло побудовано-----------------------------------')
print("****************************************************************************************")
print(" ")
print('-4----------------------димонстарція можливостей модуля graphics------------------------')
print('-------------------------малюємо статичну побудову кола---------------------------------')

from graphics import *
win = GraphWin("Окно для графики graphics", 300, 300)
obj = Oval(Point(100, 100), Point(250, 200))
obj.draw(win)
win.getMouse()
win.close()

print("****************************************************************************************")
print('-------------------------------ВІТАЮ, коло побудовано-----------------------------------')
print("****************************************************************************************")

