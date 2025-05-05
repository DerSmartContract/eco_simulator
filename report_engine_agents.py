## report_engine_agents.py ##
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "agent_results"
REPORT_DIR = BASE_DIR / "sensitivity_report"
TEMPLATES = BASE_DIR / "templates"

REPORT_DIR.mkdir(exist_ok=True)
TEMPLATES.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

def load_agent_results() -> pd.DataFrame:
    """Lädt Agenten-Simulationsergebnisse aus CSV."""
    all_files = list(RESULTS_DIR.glob("agents_results_*.csv"))
    if not all_files:
        raise FileNotFoundError("Keine Agenten-Ergebnisse gefunden.")
    df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)
    return df

def plot_agent_trends(df: pd.DataFrame):
    """Erstellt Trendplots für Population, Speed und Curiosity."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["time"], df["population"], label="Population", color="skyblue")
    ax.plot(df["time"], df["speed"], label="Ø Speed", color="blue")
    ax.plot(df["time"], df["curiosity"], label="Ø Curiosity", color="pink")
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Wert")
    ax.set_title("Agenten Evolutionstrends")
    ax.legend()
    plt.tight_layout()
    fig.savefig(REPORT_DIR / "agent_trends.png")
    plt.close(fig)

def generate_agent_report():
    df = load_agent_results()
    plot_agent_trends(df)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES)))
    tpl = env.get_template("report_template.html")
    html = tpl.render(records=df.to_dict(orient="records"))
    html_path = REPORT_DIR / "agent_report.html"
    html_path.write_text(html, encoding="utf-8")
    HTML(str(html_path)).write_pdf(str(html_path.with_suffix(".pdf")))