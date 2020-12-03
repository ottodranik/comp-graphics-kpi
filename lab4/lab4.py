import math
from graphics import *
import numpy as np
import math as mt
import matplotlib.colors as colors


# Функція проекції на xy, z=0 ------------------------------------------
def project_xy(figure):
  f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])  # по строках
  ft = f.T
  return figure.dot(ft)


def draw_pixel(x, y, canvas, color='black'):
  obj = Point(x, y)
  obj.setFill(color)
  obj.draw(canvas)


def find_max(values):
  index = 0
  value = values[0]
  for i in range(1, len(values)):
    if values[i] > value:
      index = i
      value = values[index]
  return value, index


def find_min(values):
  index = 0
  value = values[0]
  for i in range(1, len(values)):
    if values[i] < value:
      index = i
      value = values[index]
  return value, index


def fill_side_pixel_color(xp, yp, canvas, color=None):
  def fill_x(direction, y, y_index, range_x):
    for j in range(range_x):
      dx = xp[y_index] - j if direction == 'to_left' else xp[y_index] + j
      if in_polygon(dx, y, xp, yp) == 1:
        draw_pixel(dx, y, canvas, color)
      elif j == 0:
        continue
      else:
        break

  def fill_y(direction, y, y_index, range_y, range_x):
    for i in range(range_y):
      dy = y + i if direction == 'to_top' else y - i
      fill_x('to_left', dy, y_index, range_x)
      fill_x('to_right', dy, y_index, range_x)

  red, green, blue = color
  color = colors.rgb2hex((red, green, blue))
  max_y, max_y_index = find_max(yp)
  min_y, min_y_index = find_min(yp)
  max_x, _ = find_max(xp)
  min_x, _ = find_min(xp)
  range_y = math.ceil((max_y - min_y) / 2)
  range_x = int(max_x - min_x)

  fill_y('to_top', min_y, min_y_index, range_y, range_x)
  fill_y('to_bottom', max_y, max_y_index, range_y, range_x)


def draw_line_pixel_color(x1, y1, x2, y2, canvas=None, color=(0.5, 0.5, 0.5)):
  red, green, blue = color
  red = red - 0.001 if red > 0 else 0
  green = green - 0.001 if green > 0 else 0
  blue = blue - 0.001 if blue > 0 else 0
  col16 = colors.rgb2hex((red, green, blue))

  dx = x2 - x1
  dy = y2 - y1
  sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
  sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
  if dx < 0:
    dx = -dx
  if dy < 0:
    dy = -dy
  if dx > dy:
    pdx, pdy = sign_x, 0
    es, el = dy, dx
  else:
    pdx, pdy = 0, sign_y
    es, el = dx, dy
  x, y = x1, y1

  draw_pixel(x, y, canvas, '' + col16)

  error = el / 2
  t = 0
  while t < el:
    error -= es
    if error < 0:
      error += el
      x += sign_x
      y += sign_y
    else:
      x += pdx
      y += pdy
    t += 1
    draw_pixel(x, y, canvas, '' + col16)
  return draw_line_pixel_color


def in_polygon(x, y, xp, yp):
  counter = 0
  for i in range(len(xp)):
    if (
      ((yp[i] <= y and y < yp[i - 1]) or (yp[i - 1] <= y and y < yp[i]))
      and (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])
    ):
      counter = 1 - counter
  return counter


# Аксонометрія ----------------------------------------------
def dimetric(figure, TetaG1, TetaG2):
  TetaR1 = (np.pi * TetaG1) / 180
  TetaR2 = (np.pi * TetaG2) / 180
  f1 = np.array([
    [mt.cos(TetaR1), 0, mt.sin(TetaR1), 0],
    [0, 1, 0, 0],
    [-mt.sin(TetaR1), 0, mt.cos(TetaR1), 0],
    [0, 0, 0, 0]
  ])
  ft1 = f1.T
  prxy1 = figure.dot(ft1)
  f2 = np.array([
    [1, 0, 0, 0],
    [0, mt.cos(TetaR2), -mt.sin(TetaR2), 0],
    [0, mt.sin(TetaR2), mt.cos(TetaR2), 0],
    [0, 0, 0, 0]
  ])
  ft2 = f2.T
  prxy2 = prxy1.dot(ft2)
  return project_xy(prxy2)


# Функція побудови паралелепіпеда у пиксельному вигляді -----------------------------
def plrpd_draw_pixel(prxy, canvas, colors):
  Ax = prxy[0, 0]
  Ay = prxy[0, 1]

  Bx = prxy[1, 0]
  By = prxy[1, 1]

  Ix = prxy[2, 0]
  Iy = prxy[2, 1]

  Mx = prxy[3, 0]
  My = prxy[3, 1]

  Dx = prxy[4, 0]
  Dy = prxy[4, 1]

  Cx = prxy[5, 0]
  Cy = prxy[5, 1]

  Fx = prxy[6, 0]
  Fy = prxy[6, 1]

  Ex = prxy[7, 0]
  Ey = prxy[7, 1]

  # bottom
  color = colors[0]
  draw_line_pixel_color(Ax, Ay, Bx, By, canvas, color)
  draw_line_pixel_color(Bx, By, Cx, Cy, canvas, color)
  draw_line_pixel_color(Cx, Cy, Dx, Dy, canvas, color)
  draw_line_pixel_color(Dx, Dy, Ax, Ay, canvas, color)

  fill_side_pixel_color((Ax, Bx, Cx, Dx), (Ay, By, Cy, Dy), canvas, color)

  # back
  color = colors[1]
  draw_line_pixel_color(Bx, By, Cx, Cy, canvas, color)
  draw_line_pixel_color(Cx, Cy, Fx, Fy, canvas, color)
  draw_line_pixel_color(Fx, Fy, Ix, Iy, canvas, color)
  draw_line_pixel_color(Ix, Iy, Bx, By, canvas, color)

  fill_side_pixel_color((Bx, Cx, Fx, Ix), (By, Cy, Fy, Iy), canvas, color)

  # left
  color = colors[2]
  draw_line_pixel_color(Ax, Ay, Bx, By, canvas, color)
  draw_line_pixel_color(Bx, By, Ix, Iy, canvas, color)
  draw_line_pixel_color(Ix, Iy, Mx, My, canvas, color)
  draw_line_pixel_color(Mx, My, Ax, Ay, canvas, color)

  fill_side_pixel_color((Ax, Bx, Ix, Mx), (Ay, By, Iy, My), canvas, color)

  # right
  color = colors[3]
  draw_line_pixel_color(Dx, Dy, Cx, Cy, canvas, color)
  draw_line_pixel_color(Cx, Cy, Fx, Fy, canvas, color)
  draw_line_pixel_color(Fx, Fy, Ex, Ey, canvas, color)
  draw_line_pixel_color(Ex, Ey, Dx, Dy, canvas, color)

  fill_side_pixel_color((Dx, Cx, Fx, Ex), (Dy, Cy, Fy, Ey), canvas, color)

  # front
  color = colors[4]
  draw_line_pixel_color(Ax, Ay, Dx, Dy, canvas, color)
  draw_line_pixel_color(Dx, Dy, Ex, Ey, canvas, color)
  draw_line_pixel_color(Ex, Ey, Mx, My, canvas, color)
  draw_line_pixel_color(Mx, My, Ax, Ay, canvas, color)

  fill_side_pixel_color((Ax, Dx, Ex, Mx), (Ay, Dy, Ey, My), canvas, color)

  # top
  color = colors[5]
  draw_line_pixel_color(Mx, My, Ix, Iy, canvas, color)
  draw_line_pixel_color(Ix, Iy, Fx, Fy, canvas, color)
  draw_line_pixel_color(Fx, Fy, Ex, Ey, canvas, color)
  draw_line_pixel_color(Ex, Ey, Mx, My, canvas, color)

  fill_side_pixel_color((Mx, Ix, Fx, Ex), (My, Iy, Fy, Ey), canvas, color)

  return plrpd_draw_pixel
