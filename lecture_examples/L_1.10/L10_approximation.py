# --- Приклад_2 векторизація дискретних даних за різними алгоритмами інтерполяції та апроксимації ---------
# ------------------ Приклад А - проста інтерполяція даних
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
# ----- формування вхідного потоку дискретних даних
x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
# ----- відображення вхідного потоку дискретних даних
plt.plot(x, y,'o')
plt.show()
# ----- інтерполяуція вхідного потоку дискретних даних
f1 = interpolate.interp1d(x, y,kind = 'linear')
f2 = interpolate.interp1d(x, y, kind = 'cubic')
xnew = np.linspace(0, 4,30)
# ----- відображення інтерпольованих дискретних даних
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')
plt.show()

# --------- Приклад В - кубічна інтерполяція даних заданих періодичною кривою
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

# генерація масиву дискретних даних
x = np.linspace(0, 10, 10)
y = np.sin(x)

# побудова сплайна через масиву дискретних точок
tck = interpolate.splrep(x, y)
x2 = np.linspace(0, 10, 200)
y2 = interpolate.splev(x2, tck)

# коригування вимірювальної сітки сплайн - апроксимації
knots = np.array([x[1]])
weights = np.concatenate(([1],np.ones(x.shape[0]-2)*.01,[1]))
tck = interpolate.splrep(x, y, t=knots, w=weights)
x3 = np.linspace(0, 10, 200)
y3 = interpolate.splev(x2, tck)

# побудова графіку апроксимаційних кривих
plt.plot(x, y, 'go', x2, y2, 'b', x3, y3,'r')
plt.show()

# --------- Приклад С - інтерполяція декількома типами ----------------------------

import numpy as np
from scipy import interpolate

def sampleCubicSplinesWithDerivative(points, tangents, resolution):

       resolution = float(resolution)
       points = np.asarray(points)
       nPoints, dim = points.shape

       # формування масиву вхідних даних
       dp = np.diff(points, axis=0)                 # дискретність функції
       dp = np.linalg.norm(dp, axis=1)              # дискретність аргументу
       d = np.cumsum(dp)                            # діапазон зміни аргументу
       d = np.hstack([[0],d])                       # корегування відносно початку
       l = d[-1]                                    # загальний обсяг масиву
       nSamples = int(l/resolution)                 # кількість елементів вибірки
       s,r = np.linspace(0,l,nSamples,retstep=True) # параметр, крок

       # корегування форматів
       assert(len(points) == len(tangents))
       data = np.empty([nPoints, dim], dtype=object)
       for i,p in enumerate(points):
           t = tangents[i]

           assert(t is None or len(t)==dim)
           fuse = list(zip(p,t) if t is not None else zip(p,))
           data[i,:] = fuse

       # Обчислення сплайму
       samples = np.zeros([nSamples, dim])
       for i in range(dim):
           poly = interpolate.BPoly.from_derivatives(d, data[:,i])
           samples[:,i] = poly(s)
       return samples

# Сегмент вхідних даних
points = []
tangents = []
resolution = 0.2
points.append([0.,0.]); tangents.append([1,1])
points.append([3.,4.]); tangents.append([1,0])
points.append([5.,2.]); tangents.append([0,-1])
points.append([3.,0.]); tangents.append([-1,-1])
points = np.asarray(points)
tangents = np.asarray(tangents)

# Інтерполяція зі змінними параметрами дотичної в одному напрямку
scale = 1.
tangents1 = np.dot(tangents, scale*np.eye(2))
samples1 = sampleCubicSplinesWithDerivative(points, tangents1, resolution)
scale = 2.
tangents2 = np.dot(tangents, scale*np.eye(2))
samples2 = sampleCubicSplinesWithDerivative(points, tangents2, resolution)
scale = 3.
tangents3 = np.dot(tangents, scale*np.eye(2))
samples3 = sampleCubicSplinesWithDerivative(points, tangents3, resolution)

# Графік результату
import matplotlib.pyplot as plt
plt.scatter(samples1[:,0], samples1[:,1], marker='o', label='samples1')
plt.scatter(samples2[:,0], samples2[:,1], marker='o', label='samples2')
plt.scatter(samples3[:,0], samples3[:,1], marker='o', label='samples3')
plt.scatter(points[:,0], points[:,1], s=100, c='k', label='input')
plt.axis('equal')
plt.title('Interpolation')
plt.legend()
plt.show()




