##analyze_results.py##
import pandas as pd
from pathlib import Path

RESULTS_DIR = Path("sensitivity_results")

def extract_parameters(filename):
    parts = filename.replace("results_", "").replace(".csv", "").split("_")
    param_dict = {}
    for i in range(0, len(parts), 2):
        key = parts[i]
        try:
            val = float(parts[i+1])
        except (IndexError, ValueError):
            val = None
        param_dict[key] = val
    return param_dict

def classify_stability(row):
    if "prey" in row and "predator" in row and "virus" in row:
        if row["prey"] > 20 and row["predator"] > 5:
            return "Stable"
        elif row["prey"] < 5 or row["virus"] > 50:
            return "Critical"
        else:
            return "Unstable"
    elif "population" in row:
        if row["population"] > 10:
            return "Stable"
        elif row["population"] < 2:
            return "Critical"
        else:
            return "Unstable"
    else:
        return "Unknown"

def load_results():
    records = []
    for file in RESULTS_DIR.glob("results_*.csv"):
        df = pd.read_csv(file)
        final = df.iloc[-1]
        params = extract_parameters(file.name)
        stability = classify_stability(final)
        records.append({**params, **final.to_dict(), "Stability": stability})
    return pd.DataFrame(records)

if __name__ == "__main__":
    df = load_results()
    print(df)