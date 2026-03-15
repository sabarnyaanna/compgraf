import numpy as np
import matplotlib.pyplot as plt


variants = [
    {"k": 2, "a": 1},
    {"k": 4, "a": 1},
    {"k": 3, "a": 2},
    {"k": 8, "a": 4},
]

fig, axes = plt.subplots(2, 4, figsize=(16, 8), subplot_kw={"projection": "polar"})
fig.suptitle("Полярні графіки: r = a·cos(k·θ) та r = a·sin(k·θ)", fontsize=14)
theta = np.linspace(0, 2 * np.pi, 1000)
for i, v in enumerate(variants):
    k = v["k"]
    a = v["a"]

    ax_top = axes[0][i]
    r_cos = a * np.cos(k * theta)
    ax_top.plot(theta, r_cos, color="black", linewidth=1)
    ax_top.set_title(f"cos: k={k}, a={a}", pad=10)
    ax_top.set_yticklabels([]) 
    ax_top.set_xticklabels([])   
    ax_top.grid(False)           

    ax_bot = axes[1][i]
    r_sin = a * np.sin(k * theta)
    ax_bot.plot(theta, r_sin, color="black", linewidth=1)
    ax_bot.set_title(f"sin: k={k}, a={a}", pad=10)
    ax_bot.set_yticklabels([])
    ax_bot.set_xticklabels([])
    ax_bot.grid(False)

plt.tight_layout()
plt.show()
