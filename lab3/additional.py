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
