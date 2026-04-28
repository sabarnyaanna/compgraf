import numpy as np
import matplotlib.pyplot as plt


def b_spline_segment(P0, P1, P2, P3, num=50):
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


def b_spline_curve(points):
    curve = []

    n = len(points)

    for i in range(n - 3):
        seg = b_spline_segment(points[i], points[i+1], points[i+2], points[i+3])
        curve.extend(seg)

    return np.array(curve)


# =========================

# введення точок
m = int(input("Введи кількість точок: "))

points = []
for i in range(m):
    x = float(input(f"x{i}: "))
    y = float(input(f"y{i}: "))
    points.append(np.array([x, y]))

points = np.array(points)

curve = b_spline_curve(points)

# малювання
plt.plot(curve[:, 0], curve[:, 1], 'b')
plt.plot(points[:, 0], points[:, 1], 'ro--')

plt.title("Складена B-сплайн крива")
plt.grid()
plt.show()