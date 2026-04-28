import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

variants = [
    {"k": 2, "a": 1}, {"k": 4, "a": 1},
    {"k": 3, "a": 2}, {"k": 8, "a": 4},
]

fig = make_subplots(
    rows=2, cols=4,
    subplot_titles=[f"cos: k={v['k']}, a={v['a']}" for v in variants] +
                   [f"sin: k={v['k']}, a={v['a']}" for v in variants],
    specs=[[{'type': 'polar'}]*4, [{'type': 'polar'}]*4],
    vertical_spacing=0.12
)

theta = np.linspace(0, 360, 1000)

for i, v in enumerate(variants):
    k, a = v["k"], v["a"]
    rad_theta = np.radians(k * theta)

    fig.add_trace(go.Scatterpolar(
        r=a * np.cos(rad_theta),
        theta=theta,
        mode='lines',
        line=dict(color='#1f77b4', width=2.5),
        name=f"cos k={k}"
    ), row=1, col=i+1)

    fig.add_trace(go.Scatterpolar(
        r=a * np.sin(rad_theta),
        theta=theta,
        mode='lines',
        line=dict(color='#ff7f0e', width=2.5),
        name=f"sin k={k}"
    ), row=2, col=i+1)

fig.update_layout(
    title=dict(
        text="Аналіз полярних функцій: Rose Curves",
        x=0.5,
        font=dict(size=20)
    ),
    showlegend=False,
    height=850,
    width=1200,
    template="plotly_white"
)

fig.update_polars(
    radialaxis=dict(showticklabels=False, ticks=""),
    angularaxis=dict(showticklabels=True, ticks="outside", rotation=90, direction="counterclockwise")
)

fig.show()