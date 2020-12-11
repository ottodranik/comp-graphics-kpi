import numpy as np
import math as mt
from graphics import *


# Функція проекції на xy, z=0 ------------------------------------------
def draw_pixel(x, y, canvas, color='black'):
  obj = Point(x, y)
  obj.setFill(color)
  obj.draw(canvas)


def draw_line(x1, y1, x2, y2, canvas):
  # -------- Алгоритм Брезенхема ----------------
  # ------------- Малюємо початкову лінію
  # ------------- та заповнюємо масив вузлових точок для Лагранжа
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
  error, t = el / 2, 0

  x_ar = [x]  # записуємо початкове значення x
  y_ar = [y]  # записуємо початкове значення y
  steps = 4   # кількість вузлових точок

  obj = Point(x, y)
  obj.setFill('orange')
  obj.draw(canvas)

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
    draw_pixel(x, y, canvas, 'orange')
    s_amount = int(el / steps)
    if (t / s_amount != steps) and (t % s_amount == 0):
      x_ar.append(x)                          # Заповнюємо масив вузлових точок:
      y_ar.append(y)                          # якщо t кратне умові
                                              # та якщо це не остання точка в проміжку

  x_ar.append(x2)  # записуємо кінцеве значення x2
  y_ar.append(y2)  # записуємо кінцеве значення y2
  draw_pixel(x2, y2, canvas, 'orange')

  if dx >= dy:  # знаходимо y для x або x для y в залежності від значеннь dx та dy
    lagrange_build(x_ar, y_ar, int(x1), int(x2), sign_x, canvas)
  else:
    lagrange_build(y_ar, x_ar, int(y1), int(y2), sign_y, canvas, True)


# -------- Алгоритм Лагранжа ------------------
def lagrange_build(first_ar, second_ar, begin, end, step, canvas, by_y=False):
  # -------- для кожного first знаходимо second ----------
  mm = len(first_ar)
  nn = mm - 1
  for k in range(begin, end, step):  # для кожного x у проміжку
    first_p = k
    second_p = 0
    for i in range(nn + 1):
      p = 1
      for j in range(nn + 1):
        if i != j:
          p *= (first_p - first_ar[j]) / (first_ar[i] - first_ar[j])
      second_p += second_ar[i] * p
    if by_y:
      xp = second_p
      yp = first_p
    else:
      yp = second_p
      xp = first_p
    draw_pixel(xp, yp, canvas, 'violet')
  # ---------------------------------------------
  return lagrange_build


# Орт проекція ----------------------------------------------
def project_xy(Figure):
  f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])  # по строках
  ft = f.T
  return Figure.dot(ft)


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
      [0, mt.sin(TetaR2),  mt.cos(TetaR2), 0],
      [0, 0, 0, 0]
    ])
    ft2 = f2.T
    prxy2 = prxy1.dot(ft2)
    return project_xy(prxy2)  # проекція


# Функція побудови піраміди -----------------------------
def pyramid_draw_lagrange(prxy, canvas):
    Ax = prxy[0, 0]
    Ay = prxy[0, 1]

    Bx = prxy[1, 0]
    By = prxy[1, 1]

    Cx = prxy[2, 0]
    Cy = prxy[2, 1]

    Ix = prxy[3, 0]
    Iy = prxy[3, 1]

    # ----------- перша грань -------------------------------------
    draw_line(Ax, Ay, Ix, Iy, canvas)
    draw_line(Ix, Iy, Bx, By, canvas)
    draw_line(Bx, By, Ax, Ay, canvas)
    # ----------- друга грань -------------------------------------
    draw_line(Ax, Ay, Ix, Iy, canvas)
    draw_line(Ix, Iy, Cx, Cy, canvas)
    draw_line(Cx, Cy, Ax, Ay, canvas)
    # ----------- третя грань -------------------------------------
    draw_line(Bx, By, Ix, Iy, canvas)
    draw_line(Ix, Iy, Cx, Cy, canvas)
    draw_line(Cx, Cy, Bx, By, canvas)
    return pyramid_draw_lagrange


# Параметри піраміди ------------------------------------
xw = 600
yw = 600
st = 130
TetaG1 = 120
TetaG2 = 20

pyramid = np.array([  # Розташування координат у строках
  [st/2, 0, 0, 1],
  [-st/3, 0, st/3, 1],
  [-st/3, 0, -st/3, 1],
  [0, st * 1.5, 0, 1],
])  # по строках

win = GraphWin("3D векторної піраміди аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('gray')
win.setCoords(-250, -250, 250, 250)
final_pyramid = dimetric(pyramid, TetaG1, TetaG2)  # діметрія
pyramid_draw_lagrange(final_pyramid, win)  # малюємо растр та вектор

win.getMouse()
win.close()


