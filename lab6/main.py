import numpy as np
from graphics import GraphWin
from lab6 import plrpd_draw_lagrange, dimetric, draw_background

# Параметри паралелепіпеда ------------------------------------
xw = 600
yw = 600
st = 130
TetaG1 = 120
TetaG2 = 10

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

win = GraphWin("Фрактали Сєрпінського та Мандельброта", xw, yw, autoflush=False)
win.setBackground('#253582')
win.setCoords(-250, -250, 250, 250)

# Намалювати та зберегти фонове зображення ------
draw_background(win)

# Намалювати 3D паралелепіпед ------
prlpd = dimetric(prlpd, TetaG1, TetaG2)
colors = [(0, 1, 1), (0, 0, 1), (1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 1)]
plrpd_draw_lagrange(prlpd, win, colors)

win.getMouse()
win.close()
