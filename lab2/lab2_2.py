import numpy as np
import math as mt
from lab2_utils import get_point, get_center

# Create input vector
def create_input_vector(x, y):
  return np.array([[x, y]])

# Move point
def calc_move(input_matrix, params):
  dx = params.get('dx')
  dy = params.get('dy')
  f = np.array([[dx, -dy]])
  return np.sum([input_matrix, f], axis=0)

# Turn point around OXY center
def calc_turn(input_matrix, params):
  TetaR = params.get('TetaR')
  fp = np.array([
    [mt.cos(TetaR), -mt.sin(TetaR)],
    [mt.sin(TetaR), mt.cos(TetaR)]
  ])
  ftp = fp.T
  return input_matrix.dot(ftp)

# Move point to appropriate place around the OXY center, turn around OXY center and move back
def calc_rotate(input_matrix, params):
  TetaR = params.get('TetaR')
  dx = params.get('dx')
  dy = params.get('dy')
  move_to_oxy_matrix = calc_move(input_matrix, {'dx': -dx, 'dy': dy})  # move point into the center of OXY
  rotate_on_oxy_matrix = calc_turn(move_to_oxy_matrix, {'TetaR': TetaR})  # rotate point around the center of OXY
  move_back_matrix = calc_move(rotate_on_oxy_matrix, {'dx': dx, 'dy': -dy})  # move back into the real place
  return move_back_matrix


# Rotate figure
def rotate(*points, **params):
  TetaR = params.get('TetaR')
  center_x, center_y = get_center(points)
  final = []
  for i in range(len(points)):
    vector = create_input_vector(points[i][0], points[i][1])  # input vector
    rotate_matrix = calc_rotate(vector, {'dx': center_x, 'dy': center_y, 'TetaR': TetaR})
    new_point = get_point(rotate_matrix)  # get new x,y of point
    final.append(new_point)
  return final


# Rotate and move figure
def rotate_and_move(*points, **params):
  TetaR = params.get('TetaR')
  center_x, center_y = get_center(points)
  final = []
  for i in range(len(points)):
    vector = create_input_vector(points[i][0], points[i][1])
    rotate_matrix = calc_rotate(vector, {'dx': center_x, 'dy': center_y, 'TetaR': TetaR})
    move_matrix = calc_move(rotate_matrix, params)
    new_point = get_point(move_matrix)
    final.append(new_point)
  return final
