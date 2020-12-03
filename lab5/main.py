import numpy as np
from graphics import GraphWin
from lab5 import plrpd_draw_lagrange, dimetric


# Параметри паралелепіпеда ------------------------------------
xw = 600
yw = 600
st = 130
TetaG1 = 120
TetaG2 = 20

# Розташування координат у строках:
# дальній чотирикутник - A B I M, ближній чотирикутник D C F E
prlpd = np.array([
  [0, 0, 0, 1],
  [st, 0, 0, 1],
  [st, st, 0, 1],
  [0, st, 0, 1],
  [0, 0, st, 1],
  [st, 0, st, 1],
  [st, st, st, 1],
  [0, st, st, 1]
])  # по строках

win = GraphWin("3D векторний паралелепіпеда аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('gray')
win.setCoords(-250, -250, 250, 250)
prlpd = dimetric(prlpd, TetaG1, TetaG2)
colors = [(0, 1, 1), (0, 0, 1), (1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 1)]
plrpd_draw_lagrange(prlpd, win, colors)

win.getMouse()
win.close()
