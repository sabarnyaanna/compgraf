import numpy as np
import matplotlib.pyplot as plt


def draw_rect(ax, x, y, w, h):
    rect = plt.Rectangle((x, y), w, h, fill=False, edgecolor='black')
    ax.add_patch(rect)


def fractal(ax, x, y, size, depth):
    draw_rect(ax, x, y, size, size)

    if depth == 1:
        return

    s = size / 3
    offset = s * 0.1

    # 🔴 ВСІ зміщення "вліво" відносно напрямку

    # ВЕРХ (йдемо вгору → вліво = x -)
    fractal(ax, x - s, y + size + offset, size, depth - 1)

    # ПРАВО (йдемо вправо → вліво = y +)
    fractal(ax, x + size + offset, y + s, size, depth - 1)

    # НИЗ (йдемо вниз → вліво = x +)
    fractal(ax, x + s, y - size - offset, size, depth - 1)

    # ЛІВО (йдемо вліво → вліво = y -)
    fractal(ax, x - size - offset, y - s, size, depth - 1)


# ======================

depth = int(input("Введи глибину: "))

fig, ax = plt.subplots()
ax.set_aspect('equal')

fractal(ax, 0, 0, 1, depth)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.axis('off')

plt.show()