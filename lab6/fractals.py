from graphics import *
import numpy as np

def get_sierpinski_middle(p1, p2):
  return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def sierpinski_triangle(win, points, depth):
  line1 = Line(Point(points[0][0], points[0][1]), Point(points[1][0], points[1][1]))
  line2 = Line(Point(points[1][0], points[1][1]), Point(points[2][0], points[2][1]))
  line3 = Line(Point(points[2][0], points[2][1]), Point(points[0][0], points[0][1]))
  line1.setFill('orange')
  line2.setFill('orange')
  line3.setFill('orange')
  line1.draw(win)
  line2.draw(win)
  line3.draw(win)

  if depth > 0:
    sierpinski_triangle(
      win,
      [
        points[0],
        get_sierpinski_middle(points[0], points[1]),
        get_sierpinski_middle(points[0], points[2])],
      depth - 1,
    )

    sierpinski_triangle(
      win,
      [
        points[1],
        get_sierpinski_middle(points[0], points[1]),
        get_sierpinski_middle(points[1], points[2])
      ],
      depth - 1,
    )

    sierpinski_triangle(
      win,
      [
        points[2],
        get_sierpinski_middle(points[2], points[1]),
        get_sierpinski_middle(points[0], points[2])
      ],
      depth - 1,
    )


def mandelbrot(win, offsetX, offsetY):
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
  color = 'white'
  if n > 100:
    color = 'black'
  elif n > 75:
    color = 'white'
  elif n > 50:
    color = 'red'
  elif n > 15:
    color = 'grey'
  elif n > 5:
    color = 'blue'
  if color != 'white':
    win.plot(p, q, color=color)


def draw_fractals(win):
  points = [[-250, 0], [-125, 250], [0, 0]]
  sierpinski_triangle(win, points, 5)
  mandelbrot(win, -100, 100)
