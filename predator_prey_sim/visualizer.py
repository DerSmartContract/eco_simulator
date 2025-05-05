from typing import Literal
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

def plot_time_series(
    data: dict[str, np.ndarray],
    backend: Literal["matplotlib", "plotly"] = "matplotlib",
    save: str | None = None
):
    names = ["prey","predator","bacteria","virus","immune","nutrient"]
    t = data["time"]
    if backend == "matplotlib":
        fig, ax = plt.subplots(figsize=(8,5))
        for n in names:
            ax.plot(t, data[n], label=n)
        ax.set(xlabel="Zeit", ylabel="Pop./Konz.")
        ax.legend()
        fig.tight_layout()
        if save:
            fig.savefig(save)
        else:
            plt.show()
    else:
        fig = go.Figure()
        for n in names:
            fig.add_trace(go.Scatter(x=t, y=data[n], mode="lines", name=n))
        fig.update_layout(xaxis_title="Zeit", yaxis_title="Pop./Konz.")
        if save:
            fig.write_image(save)
        else:
            fig.show()
