import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

RESULTS_DIR = Path("sensitivity_results")

def plot_population_over_time():
    for file in RESULTS_DIR.glob("results_*.csv"):
        df = pd.read_csv(file)
        plt.figure(figsize=(10, 6))
        for col in ["prey", "predator", "bacteria", "virus", "immune", "nutrient"]:
            plt.plot(df["time"], df[col], label=col)
        plt.title(f"Populationen über die Zeit\n{file.name}")
        plt.xlabel("Zeit")
        plt.ylabel("Population/Konzentration")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    plot_population_over_time()