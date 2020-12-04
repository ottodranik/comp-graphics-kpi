import numpy as np
import math as mt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import to_rgba


# Зміщення ----------------------------------------------
def shift_xyz(figure, l=0, m=0, n=0):
  f = np.array([
    [1, 0, 0, l],
    [0, 1, 0, m],
    [0, 0, 1, n],
    [1, 0, 0, 1]
  ])  # по строках
  ft = f.T
  return figure.dot(ft)


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
    return prxy2


# Функція побудови піраміди -----------------------------
def pyramid_draw(prxy, ax):
    Ax = prxy[0, 0]
    Ay = prxy[0, 1]

    Bx = prxy[1, 0]
    By = prxy[1, 1]

    Cx = prxy[2, 0]
    Cy = prxy[2, 1]

    Ix = prxy[3, 0]
    Iy = prxy[3, 1]

    obj1 = patches.Polygon([[Ax, Ay], [Bx, By], [Cx, Cy]], fc=to_rgba('#FFFF00', 0.7), ec='black')
    ax.add_patch(obj1)  # bottom
    obj2 = patches.Polygon([[Ax, Ay], [Ix, Iy], [Bx, By]], fc=to_rgba('#FF7700', 0.9), ec='black')
    ax.add_patch(obj2)  # first
    obj3 = patches.Polygon([[Bx, By], [Ix, Iy], [Cx, Cy]], fc=to_rgba('#FF0000', 0.9), ec='black')
    ax.add_patch(obj3)  # second
    obj4 = patches.Polygon([[Cx, Cy], [Ix, Iy], [Ax, Ay]], fc=to_rgba('#00FF77', 0.9), ec='black')
    ax.add_patch(obj4)  # third
    return pyramid_draw


# Зсуваємо фігуру ----------------------------------------------
def draw_figure(ax_fig, pyramid_fig, offset, Teta1, Teta2):
  x_offset, y_offset, _ = offset
  final = shift_xyz(pyramid_fig, x_offset, y_offset)  # зсув
  final = dimetric(final, Teta1, Teta2)  # діметрія
  final = project_xy(final)  # проекція
  pyramid_draw(final, ax_fig)  # малюємо піраміду
  return draw_figure


# Параметри піраміди ------------------------------------
xw = 600
yw = 600
st = 200
TetaG1 = 120
TetaG2 = 20

pyramid = np.array([  # Розташування координат у строках
  [st/2, 0, 0, 1],
  [-st/3, 0, st/3, 1],
  [-st/3, 0, -st/3, 1],
  [0, st * 1.5, 0, 1],
])  # по строках

fig = plt.figure('3D', figsize=(14, 8))
ax = fig.add_subplot()
plt.xlim(-400, 400)
plt.ylim(-400, 400)
offset_x = 0
offset_y = -200
offset_z = 0
draw_figure(ax, pyramid, (offset_x, offset_y, offset_z), TetaG1, TetaG2)
plt.draw()
plt.pause(1)
for i in range(50):
  offset_x = i * 5
  offset_y = -200 + i * 5
  offset_z = 0
  draw_figure(ax, pyramid, (offset_x, offset_y, offset_z), TetaG1, TetaG2)
  plt.draw()
  plt.pause(2)
  [p.remove() for p in reversed(ax.patches)] if i != 19 else None

plt.show()

