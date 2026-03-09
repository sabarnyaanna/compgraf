import numpy as np
import matplotlib.pyplot as plt

# Параметри для кожного з 4 варіантів
variants = [
    {"k": 2, "a": 1},
    {"k": 4, "a": 1},
    {"k": 3, "a": 2},
    {"k": 8, "a": 4},
]

# Створюємо фігуру з 8 підграфіками: 2 рядки x 4 стовпці
# subplot_kw={"projection": "polar"} — робить усі підграфіки полярними
fig, axes = plt.subplots(2, 4, figsize=(16, 8), subplot_kw={"projection": "polar"})

# Заголовок для всієї фігури
fig.suptitle("Полярні графіки: r = a·cos(k·θ) та r = a·sin(k·θ)", fontsize=14)

# Кут θ від 0 до 2π (повне коло)
theta = np.linspace(0, 2 * np.pi, 1000)

for i, v in enumerate(variants):
    k = v["k"]
    a = v["a"]

    # --- Верхній рядок: r = a * cos(k * θ) ---
    ax_top = axes[0][i]
    r_cos = a * np.cos(k * theta)
    ax_top.plot(theta, r_cos, color="black", linewidth=1)
    ax_top.set_title(f"cos: k={k}, a={a}", pad=10)
    ax_top.set_yticklabels([])   # прибираємо підписи радіуса
    ax_top.set_xticklabels([])   # прибираємо підписи кутів
    ax_top.grid(False)           # вимикаємо сітку

    # --- Нижній рядок: r = a * sin(k * θ) ---
    ax_bot = axes[1][i]
    r_sin = a * np.sin(k * theta)
    ax_bot.plot(theta, r_sin, color="black", linewidth=1)
    ax_bot.set_title(f"sin: k={k}, a={a}", pad=10)
    ax_bot.set_yticklabels([])
    ax_bot.set_xticklabels([])
    ax_bot.grid(False)

plt.tight_layout()
plt.show()
