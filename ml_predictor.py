import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path

# Modell-Speicherorte
MODEL_DIR = Path(__file__).parent / "models"
MODEL_DIR.mkdir(exist_ok=True)

PREDATOR_MODEL_PATH = MODEL_DIR / "rf_model_predator.pkl"
AGENT_MODEL_PATH    = MODEL_DIR / "rf_model_agents.pkl"

#######################################
# ----- PREDICTOR FUNKTIONEN -------- #
#######################################

def predict(alpha: float, beta: float, phi: float) -> float:
    """Alte Funktion beibehalten: Vorhersage für Predator/Prey."""
    if not PREDATOR_MODEL_PATH.exists():
        raise FileNotFoundError(f"Predator/Prey Modell fehlt: {PREDATOR_MODEL_PATH}")
    with open(PREDATOR_MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    X = np.array([[alpha, beta, phi]])
    return float(model.predict(X)[0])

def predict_predator(alpha: float, beta: float, phi: float) -> float:
    """Neue Funktion für Vorhersage von Predator/Prey."""
    return predict(alpha, beta, phi)

def predict_agent(time: float, population: float) -> float:
    """Vorhersage des durchschnittlichen Speeds in Agenten-Simulationen."""
    if not AGENT_MODEL_PATH.exists():
        raise FileNotFoundError(f"Agenten-Modell fehlt: {AGENT_MODEL_PATH}")
    with open(AGENT_MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    X = pd.DataFrame([[time, population]], columns=["time", "population"])
    return float(model.predict(X)[0])

#######################################
# -------- TRAINING FUNKTIONEN ------- #
#######################################

def train_predator_model():
    """Trainiert das Random Forest Modell für Predator/Prey Simulationen."""
    RESULTS_DIR = Path("sensitivity_results")
    records = []
    for f in RESULTS_DIR.glob("results_*.csv"):
        df = pd.read_csv(f)
        final = df.iloc[-1].to_dict()
        # Parameter aus Dateinamen extrahieren
        parts = f.stem.split("_")
        params = {parts[i]: float(parts[i+1]) for i in range(0, len(parts)-1, 2)}
        record = {**params, **final}
        records.append(record)

    if not records:
        raise ValueError("Keine Predator/Prey Ergebnisse gefunden!")

    df = pd.DataFrame(records)
    if not all(k in df.columns for k in ["alpha", "beta", "phi", "virus"]):
        raise ValueError("Benötigte Spalten alpha, beta, phi, virus fehlen in den Daten.")

    X = df[["alpha", "beta", "phi"]]
    y = df["virus"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open(PREDATOR_MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"✅ Predator/Prey Modell gespeichert: {PREDATOR_MODEL_PATH}")

def train_agent_model():
    """Trainiert das Random Forest Modell für Agenten-Simulationen."""
    RESULTS_DIR = Path("agent_results")
    all_files = list(RESULTS_DIR.glob("agents_results_*.csv"))

    if not all_files:
        raise ValueError("Keine Agenten-Ergebnisse gefunden!")

    df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)

    if not all(k in df.columns for k in ["time", "population", "speed"]):
        raise ValueError("Benötigte Spalten time, population, speed fehlen in den Agenten-Daten.")

    X = df[["time", "population"]]
    y = df["speed"]  # Ziel: Ø Speed vorhersagen

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open(AGENT_MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"✅ Agenten-Modell gespeichert: {AGENT_MODEL_PATH}")

#######################################
# ----------- INFOS ----------------- #
#######################################

def model_info():
    print("📊 Modelle:")
    print(f"- Predator/Prey Modell: {'✅ Vorhanden' if PREDATOR_MODEL_PATH.exists() else '❌ Nicht gefunden'}")
    print(f"- Agenten Modell:       {'✅ Vorhanden' if AGENT_MODEL_PATH.exists() else '❌ Nicht gefunden'}")