from graphics import *
import numpy as np
from GraphicsGroup import *

def get_sierpinski_middle(p1, p2):
  return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def sierpinski_triangle(win, group, points, depth, color):
  line1 = Line(Point(points[0][0], points[0][1]), Point(points[1][0], points[1][1]))
  line2 = Line(Point(points[1][0], points[1][1]), Point(points[2][0], points[2][1]))
  line3 = Line(Point(points[2][0], points[2][1]), Point(points[0][0], points[0][1]))
  line1.setFill(color)
  line2.setFill(color)
  line3.setFill(color)
  group.add_in_group(line1)
  group.add_in_group(line2)
  group.add_in_group(line3)

  if depth > 0:
    sierpinski_triangle(
      win,
      group,
      [
        points[0],
        get_sierpinski_middle(points[0], points[1]),
        get_sierpinski_middle(points[0], points[2])],
      depth - 1,
      color,
    )

    sierpinski_triangle(
      win,
      group,
      [
        points[1],
        get_sierpinski_middle(points[0], points[1]),
        get_sierpinski_middle(points[1], points[2])
      ],
      depth - 1,
      color,
    )

    sierpinski_triangle(
      win,
      group,
      [
        points[2],
        get_sierpinski_middle(points[2], points[1]),
        get_sierpinski_middle(points[0], points[2])
      ],
      depth - 1,
      color,
    )


def mandelbrot(win, offsetX=0, offsetY=0):
  zoom = 100
  for ip, p in enumerate(np.linspace(-2.5, 1.5, win.width - offsetX)):
    for iq, q in enumerate(np.linspace(-2, 2, win.height - offsetY)):
      c = p + 1j * q
      z = 0
      for n in range(200):
        z = z * z + c
        if abs(z) > 10:
          break
      mandelbrot_draw(win, n, p * zoom - offsetX, q * zoom - offsetY)
    win.flush()


def mandelbrot_draw(win, n, p, q):
  color = '#253582'
  if n > 100:
    color = '#042333'
  elif n > 75:
    color = 'white'
  elif n > 50:
    color = '#F68F46'
  elif n > 15:
    color = '#E8FA5B'
  elif n > 10:
    color = 'white'
  elif n > 5:
    color = '#DE7965'
  elif n > 3:
    color = '#A65C85'
  elif n > 2:
    color = '#7E4E90'
  win.plot(p, q, color=color)


def draw_fractals(win):
  mandelbrot(win, -50)

  points = [[-240, 240], [-210, 120], [-120, 210]]
  group = GraphicsGroup()
  sierpinski_triangle(win, group, points, 5, '#F9A242')
  group.draw(win)

  points = [[240, -240], [210, -120], [120, -210]]
  group = GraphicsGroup()
  sierpinski_triangle(win, group, points, 5, '#F9A242')
  group.draw(win)

  points = [[240, 240], [210, 120], [120, 210]]
  group = GraphicsGroup()
  sierpinski_triangle(win, group, points, 5, '#F9A242')
  group.draw(win)

  points = [[-240, -240], [-210, -120], [-120, -210]]
  group = GraphicsGroup()
  sierpinski_triangle(win, group, points, 5, '#F9A242')
  group.draw(win)
