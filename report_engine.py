## report_engine.py ##

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "sensitivity_results"
REPORT_DIR  = BASE_DIR / "sensitivity_report"
TEMPLATES   = BASE_DIR / "templates"

REPORT_DIR.mkdir(exist_ok=True)
TEMPLATES.mkdir(exist_ok=True)

def extract_parameters(filename: str) -> dict:
    pattern = re.compile(r'(\w+)_([0-9.]+)')
    return {k: float(v) for k, v in pattern.findall(filename)}

def load_all_results() -> pd.DataFrame:
    records = []
    for f in RESULTS_DIR.glob("results_*.csv"):
        df = pd.read_csv(f)
        final = df.iloc[-1].to_dict()
        params = extract_parameters(f.name)
        records.append({**params, **final})
    return pd.DataFrame(records)

def plot_heatmap(pivot: np.ndarray, x_vals, y_vals, filename: Path):
    fig, ax = plt.subplots()
    im = ax.imshow(pivot, origin="lower", aspect="auto")
    ax.set_xticks(range(len(x_vals))); ax.set_xticklabels(x_vals)
    ax.set_yticks(range(len(y_vals))); ax.set_yticklabels(y_vals)
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(filename)
    plt.close(fig)

def generate_report():
    df = load_all_results()
    betas = sorted(df["beta"].unique())
    phis  = sorted(df["phi"].unique())

    for var in ("virus","prey","predator"):
        piv = df.pivot(index="phi", columns="beta", values=var).values
        plot_heatmap(piv, betas, phis, REPORT_DIR / f"heatmap_{var}.png")

    env  = Environment(loader=FileSystemLoader(str(TEMPLATES)))
    tpl  = env.get_template("report_template.html")
    html = tpl.render(records=df.to_dict(orient="records"))
    html_path = REPORT_DIR / "report.html"
    html_path.write_text(html, encoding="utf-8")
    HTML(str(html_path)).write_pdf(str(html_path.with_suffix(".pdf")))
