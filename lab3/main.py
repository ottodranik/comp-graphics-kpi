import numpy as np
import matplotlib.pyplot as plt
from lab3 import plrpd_draw, rotate_custom, dimetric

# Параметри паралелепіпеда ------------------------------------
xw = 600
yw = 600
st = 200
TetaG1 = 120
TetaG2 = 20

prlpd = np.array([  # Розташування координат у строках
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
plt.xlim(-400, 400)
plt.ylim(-400, 400)
prlpd_final = dimetric(prlpd, TetaG1, TetaG2)
plrpd_draw(prlpd_final, ax)
plt.draw()
plt.pause(3)

for i in range(100):
  prlpd_final = rotate_custom(prlpd, (-10, 10, 0), 7 * i)
  prlpd_final = dimetric(prlpd_final, TetaG1, TetaG2)
  plrpd_draw(prlpd_final, ax)
  plt.draw()
  plt.pause(0.001)
  [p.remove() for p in reversed(ax.patches)] if i != 99 else None

plt.show()

