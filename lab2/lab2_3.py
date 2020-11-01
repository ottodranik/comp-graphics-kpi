import math as mt
from lab2_utils import get_center


# Move point
def calc_move(x, y, params):
  dx = params.get('dx')
  dy = params.get('dy')
  x_new = x + dx
  y_new = y + dy
  return x_new, y_new


# Turn point around OXY center
def calc_turn(x, y, params):
  TetaR = params.get('TetaR')
  x_new = x * mt.cos(TetaR) - y * mt.sin(TetaR)
  y_new = x * mt.sin(TetaR) + y * mt.cos(TetaR)
  return x_new, y_new


# Move point to appropriate place around the OXY center, turn around OXY center and move back
def calc_rotate(x, y, params):
  TetaR = params.get('TetaR')
  dx = params.get('dx')
  dy = params.get('dy')

  # move point into the center of OXY
  x_new, y_new = calc_move(x, y, {'dx': -dx, 'dy': -dy})

  # rotate point around the center of OXY
  x_new, y_new = calc_turn(x_new, y_new, {'TetaR': TetaR})

  # move back into the real place
  x_new, y_new = calc_move(x_new, y_new, {'dx': dx, 'dy': dy})
  return x_new, y_new


# Rotate figure
def rotate(*points, **params):
  TetaR = params.get('TetaR')
  center_x, center_y = get_center(points)
  final = []
  for i in range(len(points)):
    x_new, y_new = calc_rotate(points[i][0], points[i][1], {'dx': center_x, 'dy': center_y, 'TetaR': TetaR})
    final.append((x_new, y_new))
  return final


# Rotate and move figure
def rotate_and_move(*points, **params):
  TetaR = params.get('TetaR')
  dx = params.get('dx')
  dy = params.get('dy')

  center_x, center_y = get_center(points)
  final = []
  for i in range(len(points)):
    x_new, y_new = calc_rotate(points[i][0], points[i][1], {'dx': center_x, 'dy': center_y, 'TetaR': TetaR})
    x_new, y_new = calc_move(x_new, y_new, {'dx': dx, 'dy': -dy, 'TetaR': TetaR})
    final.append((x_new, y_new))
  return final

