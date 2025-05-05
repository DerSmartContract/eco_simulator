import sys
from pathlib import Path

# Hauptverzeichnis zum Importieren verfügbar machen
sys.path.append(str(Path(__file__).parent.parent))

from sensitivity_engine import batch_run

# Liste der Parameterkombinationen
param_list = [
    {"alpha": 0.18, "beta": 0.015, "phi": 0.005, "mutation_rate": 0.03, "curiosity": 0.5},
    {"alpha": 0.22, "beta": 0.018, "phi": 0.006, "mutation_rate": 0.04, "curiosity": 0.6},
    {"alpha": 0.25, "beta": 0.02, "phi": 0.005, "mutation_rate": 0.05, "curiosity": 0.4},
    {"alpha": 0.3, "beta": 0.022, "phi": 0.007, "mutation_rate": 0.06, "curiosity": 0.7}
]

if __name__ == "__main__":
    print("🔎 Sensitivitätsanalyse wird gestartet...")
    print(f"Parameter-Kombinationen ({len(param_list)} Läufe):")
    for params in param_list:
        print(" -", params)
    results = batch_run(param_list)
    print("✅ Sensitivitätsanalyse abgeschlossen. Dateien gespeichert:")
    for path in results:
        print(f" - {path}")