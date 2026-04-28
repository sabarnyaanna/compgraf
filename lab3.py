import numpy as np
import matplotlib.pyplot as plt


def b_spline_4points(P0, P1, P2, P3, num=100):
    t = np.linspace(0, 1, num)

    curve = []

    for ti in t:
        point = (
            (-ti**3 + 3*ti**2 - 3*ti + 1) * P0 +
            (3*ti**3 - 6*ti**2 + 4) * P1 +
            (-3*ti**3 + 3*ti**2 + 3*ti + 1) * P2 +
            (ti**3) * P3
        ) / 6.0

        curve.append(point)

    return np.array(curve)


# точки
P0 = np.array([0, 0])
P1 = np.array([1, 2])
P2 = np.array([3, 3])
P3 = np.array([4, 0])

curve = b_spline_4points(P0, P1, P2, P3)

# малювання
plt.plot(curve[:, 0], curve[:, 1], 'b')
plt.plot([P0[0], P1[0], P2[0], P3[0]],
         [P0[1], P1[1], P2[1], P3[1]], 'ro--')

plt.title("B-сплайн (4 точки)")
plt.grid()
plt.show()

