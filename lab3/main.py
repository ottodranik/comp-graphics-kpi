import numpy as np
import matplotlib.pyplot as plt
from lab3 import plrpd_draw, rotate_custom, dimetric

# Параметри паралелепіпеда ------------------------------------
xw = 600
yw = 600
st = 200
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

fig = plt.figure('3D', figsize=(14, 8))
ax = fig.add_subplot()
plt.xlim(-500, 500); plt.ylim(-500, 500)
prlpd = dimetric(prlpd, TetaG1, TetaG2)
plrpd_draw(prlpd, ax)
plt.draw(); plt.pause(3)

for i in range(100):
  prlpd_final = rotate_custom(prlpd, (0, 10, 10), 7 * i)
  plrpd_draw(prlpd_final, ax)
  plt.draw()
  plt.pause(0.01)
  if i != 99:
    [p.remove() for p in reversed(ax.patches)]
plt.show()

