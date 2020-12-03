from graphics import *
import numpy as np
import math as mt
from PIL import Image as NewImage
from fractals import draw_fractals


def clear(win):
  for item in win.items[:]:
    item.undraw()
  win.update()
  win.flush()


# Функція проекції на xy, z=0 ------------------------------------------
def project_xy(figure):
  f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])  # по строках
  ft = f.T
  return figure.dot(ft)


def draw_pixel(x, y, canvas, color='black'):
  obj = Point(x, y)
  obj.setFill(color)
  obj.draw(canvas)
  canvas.update()
  canvas.flush()


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
    s_amount = int(dx / steps)
    if dx != 0 and t / s_amount != steps and t % s_amount == 0:
      x_ar.append(x)                          # Заповнюємо масив вузлових точок:
      y_ar.append(y)                          # якщо t кратне умові, якщо dx не 0,
                                              # та якщо це не остання точка в проміжку

  x_ar.append(x2)  # записуємо кінцеве значення x2
  y_ar.append(y2)  # записуємо кінцеве значення y2

  if dx != 0:
    lagrange_build(x_ar, y_ar, int(x1), int(x2), sign_x, canvas)
  else:
    for k in range(int(y1), int(y2), sign_y):
      draw_pixel(x1, k, canvas, 'orange')


# -------- Алгоритм Лагранжа ------------------
def lagrange_build(x_ar, y_ar, begin, end, step, canvas):
  # -------- для кожного x знаходимо y ----------
  mm = len(x_ar)
  nn = mm - 1
  for k in range(begin, end, step):  # для кожного x у проміжку
    xp = k
    yp = 0
    for i in range(nn + 1):
      p = 1
      for j in range(nn + 1):
        if i != j:
          p *= (xp - x_ar[j]) / (x_ar[i] - x_ar[j])
      yp += y_ar[i] * p
    draw_pixel(xp, yp, canvas, 'orange')
  # ---------------------------------------------
  return lagrange_build


# Функція побудови паралелепіпеда у пиксельному вигляді -----------------------------
def plrpd_draw_lagrange(prxy, canvas, colors=None):
  # ----------- дальня грань - (в проекції ліва) -------------------------------------
  Ax = prxy[0, 0]
  Ay = prxy[0, 1]
  Bx = prxy[1, 0]
  By = prxy[1, 1]
  Ix = prxy[2, 0]
  Iy = prxy[2, 1]
  Mx = prxy[3, 0]
  My = prxy[3, 1]
  # ----------- ближня грань - (в проекції права) -------------------------------------
  Dx = prxy[4, 0]
  Dy = prxy[4, 1]
  Cx = prxy[5, 0]
  Cy = prxy[5, 1]
  Fx = prxy[6, 0]
  Fy = prxy[6, 1]
  Ex = prxy[7, 0]
  Ey = prxy[7, 1]

  # ----------- дальня грань - (в проекції ліва) -------------------------------------
  draw_line(Ax, Ay, Bx, By, canvas)
  draw_line(Bx, By, Ix, Iy, canvas)
  draw_line(Ix, Iy, Mx, My, canvas)
  draw_line(Mx, My, Ax, Ay, canvas)
  # ----------- ближча грань - (в проекції права) -------------------------------------
  draw_line(Dx, Dy, Cx, Cy, canvas)
  draw_line(Cx, Cy, Fx, Fy, canvas)
  draw_line(Fx, Fy, Ex, Ey, canvas)
  draw_line(Ex, Ey, Dx, Dy, canvas)
  # ----------- верхеня грань - (в проекції верхня) -------------------------------------
  draw_line(Ax, Ay, Bx, By, canvas)
  draw_line(Bx, By, Cx, Cy, canvas)
  draw_line(Cx, Cy, Dx, Dy, canvas)
  draw_line(Dx, Dy, Ax, Ay, canvas)
  # ----------- нижня грань - (в проекції нижня) -------------------------------------
  draw_line(Mx, My, Ix, Iy, canvas)
  draw_line(Ix, Iy, Fx, Fy, canvas)
  draw_line(Fx, Fy, Ex, Ey, canvas)
  draw_line(Ex, Ey, Mx, My, canvas)
  # ----------- ліва грань - (в проекції ближня) ----------------------------------------
  draw_line(Ax, Ay, Mx, My, canvas)
  draw_line(Mx, My, Ex, Ey, canvas)
  draw_line(Ex, Ey, Dx, Dy, canvas)
  draw_line(Dx, Dy, Ax, Ay, canvas)
  # ----------- права грань - (в проекції дальня) ----------------------------------------
  draw_line(Bx, By, Ix, Iy, canvas)
  draw_line(Ix, Iy, Fx, Fy, canvas)
  draw_line(Fx, Fy, Cx, Cy, canvas)
  draw_line(Cx, Cy, Bx, By, canvas)

  return plrpd_draw_lagrange


# Намалювати фонове зображення ------------------------
def draw_background(canvas=None):
  # Намалювати фрактали та зберегти як картинку --------
  draw_fractals(canvas)
  canvas.postscript(file="bg.eps", colormode='color')
  img = NewImage.open("bg.eps")
  img.save("bg.gif")

  # Очистити вікно ------------------------------------
  clear(canvas)

  # Застосувати збережену картинку як фонове зображення ----------
  b = Image(Point(0, 0), "bg.gif")
  Image.draw(b, canvas)
