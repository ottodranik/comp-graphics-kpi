import numpy as np
import math as mt
import matplotlib.patches as patches
from matplotlib.colors import to_rgba


# Функція проекції на xy, z=0 ------------------------------------------
def project_xy(figure):
  f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])  # по строках
  ft = f.T
  return figure.dot(ft)


# Обертання коло довільної вісі ----------------------------------------
def rotate_custom(figure, axis, TetaG):
    TetaR = (np.pi*TetaG)/180
    l, m, n = axis
    r = mt.sqrt(mt.pow(l, 2) + mt.pow(m, 2) + mt.pow(n, 2))
    T1 = np.array([[1, 0, 0, -l], [0, 1, 0, -m], [0, 0, 1, -n], [0, 0, 0, 1]])
    T2 = np.array([[1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [0, 0, 0, 1]])
    n1 = l / r
    n2 = m / r
    n3 = n / r
    R = np.array([
      [
        mt.pow(n1, 2) + (1 - mt.pow(n1, 2)) * mt.cos(TetaR),
        n1 * n2 * (1 - mt.cos(TetaR)) - n3 * mt.sin(TetaR),
        n1 * n3 * (1 - mt.cos(TetaR)) + n2 * mt.sin(TetaR),
        0,
      ],
      [
        n1 * n2 * (1 - mt.cos(TetaR)) + n3 * mt.sin(TetaR),
        mt.pow(n2, 2) + (1 - mt.pow(n2, 2)) * mt.cos(TetaR),
        n2 * n3 * (1 - mt.cos(TetaR)) - n1 * mt.sin(TetaR),
        0,
      ],
      [
        n1 * n3 * (1 - mt.cos(TetaR)) - n2 * mt.sin(TetaR),
        n2 * n3 * (1 - mt.cos(TetaR)) + n1 * mt.sin(TetaR),
        mt.pow(n3, 2) + (1 - mt.pow(n3, 2)) * mt.cos(TetaR),
        0,
      ],
      [0, 0, 0, 1]
    ])
    return figure.dot(T1.T).dot(R.T).dot(T2.T)


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
    return project_xy(prxy2)


# Функція побудови паралелепіпеда -----------------------------
def plrpd_draw(prxy, ax):
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

    obj3 = patches.Polygon([[Ax, Ay], [Bx, By], [Cx, Cy], [Dx, Dy]], fc=to_rgba('#FFFF00', 0.7), ec='black')
    ax.add_patch(obj3)  # bottom
    obj6 = patches.Polygon([[Bx, By], [Cx, Cy], [Fx, Fy], [Ix, Iy]], fc=to_rgba('#00FFFF', 0.9), ec='black')
    ax.add_patch(obj6)  # back
    obj2 = patches.Polygon([[Dx, Dy], [Cx, Cy], [Fx, Fy], [Ex, Ey]], fc=to_rgba('#FF7700', 0.7), ec='black')
    ax.add_patch(obj2)  # right
    obj1 = patches.Polygon([[Ax, Ay], [Bx, By], [Ix, Iy], [Mx, My]], fc=to_rgba('#FF0000', 0.9), ec='black')
    ax.add_patch(obj1)  # left
    obj5 = patches.Polygon([[Ax, Ay], [Dx, Dy], [Ex, Ey], [Mx, My]], fc=to_rgba('#00FF77', 0.7), ec='black')
    ax.add_patch(obj5)  # front
    obj4 = patches.Polygon([[Mx, My], [Ix, Iy], [Fx, Fy], [Ex, Ey]], fc=to_rgba('#00FF00', 0.9), ec='black')
    ax.add_patch(obj4)  # top
    return plrpd_draw
