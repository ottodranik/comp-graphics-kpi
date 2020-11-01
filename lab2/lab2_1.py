import numpy as np
import math as mt
from lab2_utils import get_point, get_center


# Create input vector
def create_input_vector(x, y):
  return np.array([
    [x, y, 1]
  ])


# Init MOVE matrix according to dx and dy
def create_move_matrix(dx, dy):
  f = np.array([
    [1, 0, dx],
    [0, 1, -dy],
    [0, 0, 1]
  ])
  return f.T


# Init TURN matrix according to TetaR
def create_turn_matrix(TetaR):
  fp = np.array([
    [mt.cos(TetaR), -mt.sin(TetaR), 0],
    [mt.sin(TetaR), mt.cos(TetaR), 0],
    [0, 0, 1]
  ])
  return fp.T


# Move point to appropriate place around the OXY center, turn around OXY center and move back
def calc_rotate(input_matrix, params):
  TetaR = params.get('TetaR')
  center_x = params.get('dx')
  center_y = params.get('dy')
  move_oxy_m = create_move_matrix(-center_x, center_y)
  turn_m = create_turn_matrix(TetaR)
  move_back_m = create_move_matrix(center_x, -center_y)
  return input_matrix.dot(move_oxy_m).dot(turn_m).dot(move_back_m)

# Rotate figure (MOVE to oxy + TURN + MOVE back)
def rotate(*points, **params):
  TetaR = params.get('TetaR')
  center_x, center_y = get_center(points)
  final = []
  for i in range(len(points)):
    vector = create_input_vector(points[i][0], points[i][1])  # input vector
    final_m = calc_rotate(vector, {'dx': center_x, 'dy': center_y, 'TetaR': TetaR})
    new_point = get_point(final_m)  # get new x,y of point
    final.append(new_point)
  return final

# Rotate and move figure
def rotate_and_move(*points, **params):
  TetaR = params.get('TetaR')
  dx = params.get('dx')
  dy = params.get('dy')
  center_x, center_y = get_center(points)
  final = []
  for i in range(len(points)):
    vector = create_input_vector(points[i][0], points[i][1])
    move_matrix = create_move_matrix(dx, dy)
    final_m = calc_rotate(vector, {'dx': center_x, 'dy': center_y, 'TetaR': TetaR}).dot(move_matrix)
    new_point = get_point(final_m)
    final.append(new_point)
  return final

