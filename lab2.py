import numpy as np
import matplotlib.pyplot as plt


def get_fractal_step(p1, p2, depth):
    # Глибина 1: просто сторона квадрата
    if depth <= 1:
        return [p1, p2]

    # Вектори для розрахунку (u - вздовж сторони, n - перпендикуляр)
    v = p2 - p1
    u = v / 3.0
    # Нормаль (поворот на 90 градусів)
    n = np.array([-u[1], u[0]])

    # ТВОЯ СХЕМА (7 точок на кожну сторону):
    # 1. Піднімаємося вгору назовні
    # 2. Проходимо 1/3 паралельно
    # 3. Спускаємося вниз (перетинаємо основну лінію)
    # 4. Проходимо 1/3 паралельно всередині
    # 5. Повертаємося на фінішну точку

    p_a = p1 + n  # Вгору від старту
    p_b = p_a + u  # Вперед вгорі
    p_c = p_b - n  # Спуск на основну лінію (1/3 шляху)
    p_d = p_c - n  # Спуск ще нижче (всередину)
    p_e = p_d + u  # Вперед внизу
    p_f = p_e + n  # Повернення на лінію (2/3 шляху)
    # p2 — фініш (3/3 шляху)

    if depth > 2:
        # Для вищих рівнів рекурсії ділимо кожен відрізок далі
        segments = [(p1, p_a), (p_a, p_b), (p_b, p_c), (p_c, p_d), (p_d, p_e), (p_e, p_f), (p_f, p2)]
        points = []
        for s_start, s_end in segments:
            points.extend(get_fractal_step(s_start, s_end, depth - 1)[:-1])
        points.append(p2)
        return points
    else:
        return [p1, p_a, p_b, p_c, p_d, p_e, p_f, p2]


def main():
    try:
        depth = int(input("Введіть глибину (1 - квадрат, 2 - твоя схема): "))
    except:
        depth = 1

    # Початковий квадрат (чисті координати)
    size = 300
    pts = [np.array([0, size]), np.array([size, size]), np.array([size, 0]), np.array([0, 0])]

    final_points = []
    for i in range(4):
        p_start = pts[i]
        p_end = pts[(i + 1) % 4]
        res = get_fractal_step(p_start, p_end, depth)
        final_points.extend(res[:-1])

    final_points.append(final_points[0])  # Точне замикання
    data = np.array(final_points)

    plt.figure(figsize=(8, 8))
    plt.plot(data[:, 0], data[:, 1], 'k-', lw=2)  # Чорна чітка лінія
    plt.fill(data[:, 0], data[:, 1], 'cyan', alpha=0.1)
    plt.axis('equal')
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.title(f"Твоя схема (Глибина {depth})")
    plt.show()


if __name__ == "__main__":
    main()