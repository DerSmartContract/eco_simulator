import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ----------------------------- CONFIG -----------------------------
RESULTS_DIR = Path("sensitivity_results")

# ----------------------------- CSV LADEN -----------------------------
def load_all_results():
    csv_files = list(RESULTS_DIR.glob("results_*.csv"))
    if not csv_files:
        raise FileNotFoundError("Keine CSV-Dateien im Verzeichnis 'sensitivity_results' gefunden.")

    dfs = []
    for file in csv_files:
        df = pd.read_csv(file)
        params = file.stem.replace("results_", "").split("_")
        df["beta"] = float(params[0])
        df["phi"] = float(params[1])
        df["alpha"] = float(params[2])
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

# ----------------------------- STATISTIK -----------------------------
def summarize(df):
    print("\n▶ Allgemeine Statistik:")
    print(df.describe())
    print("\n▶ Parameterbereiche:")
    print("Alpha:", df["alpha"].unique())
    print("Beta:", df["beta"].unique())
    print("Phi:", df["phi"].unique())

# ----------------------------- KORRELATION -----------------------------
def plot_correlation(df):
    populations = ["prey", "predator", "bacteria", "virus", "immune", "nutrient"]
    corr = df[populations].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="viridis", fmt=".2f")
    plt.title("Korrelation zwischen Populationen")
    plt.tight_layout()
    plt.show()

# ----------------------------- TRENDS -----------------------------
def plot_population_trends(df):
    populations = ["prey", "predator", "bacteria", "virus", "immune", "nutrient"]
    mean_populations = df.groupby("time")[populations].mean()

    plt.figure(figsize=(10, 6))
    for pop in populations:
        plt.plot(mean_populations.index, mean_populations[pop], label=pop)
    plt.xlabel("Zeit")
    plt.ylabel("Durchschnittliche Population / Konzentration")
    plt.title("Entwicklung der Populationen über die Zeit")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ----------------------------- PARAMETER-WIRKUNG -----------------------------
def plot_parameter_effects(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="alpha", y="prey", hue="beta", size="phi", sizes=(50, 200))
    plt.title("Beutepopulation in Abhängigkeit von Alpha, Beta & Phi")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ----------------------------- MAIN -----------------------------
def main():
    print("🔍 Lade CSV-Daten ...")
    df = load_all_results()

    summarize(df)

    print("\n📊 Erstelle Korrelation Heatmap ...")
    plot_correlation(df)

    print("\n📈 Erstelle Populations-Trends ...")
    plot_population_trends(df)

    print("\n📉 Analyse der Parameter-Effekte ...")
    plot_parameter_effects(df)

if __name__ == "__main__":
    main()