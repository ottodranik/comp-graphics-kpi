import numpy as np
import math as mt


# Функция проекції на xy, z=0 -------------------------------------
def project_xy(Figure):
  f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])  # по строках
  ft = f.T
  Prxy = Figure.dot(ft)
  print('проекция на ху')
  print(Prxy)
  return Prxy


# Зміщення ----------------------------------------------
def shift_xyz(Figure, l, m, n):
  f = np.array([[1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [1, 0, 0, 1]])  # по строках
  ft = f.T
  Prxy = Figure.dot(ft)
  print('зміщення')
  print(Prxy)
  return Prxy


# Обертання коло х ----------------------------------------
def rotate_x(Figure, TetaG):
  TetaR = (np.pi * TetaG) / 180
  f = np.array(
    [[1, 0, 0, 0], [0, mt.cos(TetaR), -mt.sin(TetaR), 0], [0, mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 0, 1]])
  ft = f.T
  Prxy = Figure.dot(ft)
  print('обертання коло х')
  print(Prxy)
  return Prxy


# Обертання коло y ----------------------------------------
def rotate_y(Figure, TetaG):
  TetaR = (np.pi * TetaG) / 180
  f = np.array(
    [[mt.cos(TetaR), 0, mt.sin(TetaR), 0], [0, 1, 0, 0], [-mt.sin(TetaR), 0, mt.cos(TetaR), 0], [0, 0, 0, 1]])
  ft = f.T
  Prxy = Figure.dot(ft)
  print('обертання коло y')
  print(Prxy)
  return Prxy


# Обертання коло z----------------------------------------
def rotate_z(Figure, TetaG):
  TetaR = (np.pi * TetaG) / 180
  f = np.array(
    [[mt.cos(TetaR), -mt.sin(TetaR), 0, 0], [mt.sin(TetaR), mt.cos(TetaR), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
  ft = f.T
  Prxy = Figure.dot(ft)
  print('обертання коло y')
  print(Prxy)
  return Prxy

def clear(win):
  for item in win.items[:]:
    item.undraw()
  win.update()




# def fill_side_pixel_color2(vertexes, canvas=None, color=(0.5, 0.5, 0.5)):
#   center_x, center_y = centroid(vertexes)
#   step_size = 1
#   P1, P2, P3, P4 = vertexes
#
#   def find_distances(p1, p2, p3, p4):
#     # Find distances between each pare of dots
#     return [
#       distance(p1, p2),
#       distance(p2, p3),
#       distance(p3, p4),
#       distance(p4, p1),
#     ]
#
#   def find_sign(value, center):
#     return step_size if value < center else -step_size if value > center else 0
#
#   # Find distances point between each pare of points
#   distances = find_distances(P1, P2, P3, P4)
#
#   # Find index of the smallest distance
#   min_distance = distances[0]
#   for d in distances:
#     if min_distance > d:
#       min_distance = d
#
#   # Find number of steps
#   steps = math.ceil(min_distance / (step_size * 2))
#
#   # sign of x and y to design in what direction we need to move
#   sign_xs = []
#   sign_ys = []
#   for i in range(len(vertexes)):
#     sign_xs.append(find_sign(vertexes[i][0], center_x))
#     sign_ys.append(find_sign(vertexes[i][1], center_y))
#
#   P1x, P1y = P1
#   P2x, P2y = P2
#   P3x, P3y = P3
#   P4x, P4y = P4
#
#   stop_x = False
#   stop_y = False
#   while steps > 0 and stop_x is False and stop_y is False:
#     print(steps)
#     if (steps == 47):
#       break
#     draw_line_pixel_color(P1x, P1y, P2x, P2y, canvas, color)
#     draw_line_pixel_color(P2x, P2y, P3x, P3y, canvas, color)
#     draw_line_pixel_color(P3x, P3y, P4x, P4y, canvas, color)
#     draw_line_pixel_color(P4x, P4y, P1x, P1y, canvas, color)
#     P1x += sign_xs[0]
#     P1y += sign_ys[0]
#     P2x += sign_xs[1]
#     P2y += sign_ys[1]
#     P3x += sign_xs[2]
#     P3y += sign_ys[2]
#     P4x += sign_xs[3]
#     P4y += sign_ys[3]
#
#     print((P1x, P1y), (P2x, P2y), (P3x, P3y), (P4x, P4y))
#
#     Calculate new signs of x and y for each Point
#     new_vertexes = ((P1x, P1y), (P2x, P2y), (P3x, P3y), (P4x, P4y))
#     for i in range(len(new_vertexes)):
#       sign_xs[i] = find_sign(new_vertexes[i][0], center_x)
#       sign_ys[i] = find_sign(new_vertexes[i][1], center_y)
#     steps -= 1
#     for i in sign_xs:
#       if i == step_size or i == -step_size:
#         break
#       else:
#         stop_x = True
#     for i in sign_ys:
#       if i == step_size or i == -step_size:
#         break
#       else:
#         stop_y = True
#
#     print(sign_xs, sign_ys)


# def distance(p1, p2):
#   return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# def centroid(vertexes):
#   _x_list = [vertex[0] for vertex in vertexes]
#   _y_list = [vertex[1] for vertex in vertexes]
#   _len = len(vertexes)
#   _x = sum(_x_list) / _len
#   _y = sum(_y_list) / _len
#   return (_x, _y)