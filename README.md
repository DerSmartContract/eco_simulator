

# eco_simulator

---

## Projektübersicht

**eco_simulator** ist ein hochmodulares, fortgeschrittenes Framework zur Simulation, Analyse und Prognose komplexer ökologischer Systeme.  
Es verbindet agentenbasierte Evolution, erweiterte Räuber-Beute-Dynamiken, fortschrittliche Sensitivitätsanalysen, ML-gestützte Vorhersagemodelle und eine vollständig interaktive Visualisierungs- und Steuerungskomponente.

---

### Einsatzbereiche

- Forschungsprojekte in Ökologie, Verhaltensbiologie und evolutionärer Dynamik  
- Datengetriebene Modellierung und KI-gestützte Prognosen  
- Entwicklung und Validierung adaptiver Agentenmodelle  
- Experimentelle KI-Systeme und simulationsgetriebene Entscheidungsfindung

---

## Repository-Beschreibung

### Kurzbeschreibung

> Evolutionäres KI-Ökosystem mit Predator-Prey-Simulation, Sensitivitätsanalyse, automatischer Berichtserstellung und agentenbasierter Evolution.

### Langbeschreibung

Dieses Repository vereint klassische ökologische Modelle mit modernen KI- und Analyseverfahren:

#### Agentenbasierte Evolution

- Organismen agieren auf einer rasterbasierten Umwelt  
- Energieabhängige Fähigkeiten  
- Neugiergesteuertes Verhalten  
- Mutation und Selektion  
- Interaktion, Reproduktion und Anpassung über Generationen

#### Predator-Prey-Simulation

- Erweiterte Lotka-Volterra-Modelle  
- Anpassbar auf komplexere Szenarien (z. B. Viren/Bakterien-Dynamiken)

#### Sensitivitätsanalysen

- Batch-Runs mit parametrischen Variationen  
- Heatmap- und 3D-Surface-Visualisierungen  
- Vollständig reproduzierbar und versionierbar

#### Maschinelles Lernen (ML)

- Integrierte Modelle (z. B. Random Forest) für Populationsprognosen und Parameteroptimierung

#### Automatische Berichtserstellung

- HTML- und PDF-Reports via Jinja2 und WeasyPrint  
- Enthält Simulationsergebnisse, Sensitivitätsanalysen und Visualisierungen

#### Interaktive Visualisierung

- **Streamlit-Frontend** für dynamische Steuerung und Echtzeit-Darstellung  
- Tabs: *Predator-Prey* und *Agenten-Evolution*

#### Dockerisierung

- Konsistente Entwicklungs- und Produktionsumgebungen  
- Minimaler Setup-Aufwand

#### Notebooks

- Explorative Analysen und Prototyping: `notebooks/exploration.ipynb`

---

## Installation & Deployment

### Lokale Installation

```bash
git clone https://github.com/<dein-user>/eco_simulator.git
cd eco_simulator

# Virtuelle Umgebung
python3 -m venv .venv
source .venv/bin/activate    # macOS/Linux
# .venv\Scripts\activate.bat # Windows

# Abhängigkeiten
pip install --upgrade pip
pip install -r requirements.txt

Alternativ mit Poetry

poetry install

Docker

docker build -t eco_simulator:2.0 .
docker run -p 8501:8501 eco_simulator:2.0

'''

⸻

Verwendung

Streamlit-App starten

streamlit run app.py

	•	Zugriff: http://localhost:8501
	•	Tabs: Predator-Prey und Agenten-Evolution

Tests ausführen

pytest --maxfail=1 -q

Sensitivitätsanalyse

python -c "from sensitivity_engine import batch_run; \
batch_run([{'alpha':0.1,'beta':0.02,'phi':0.005}])"

Bericht generieren (HTML & PDF)

python - <<'PYCODE'
import report_engine
report_engine.generate_report()
PYCODE

Output: sensitivity_report/report.pdf

⸻

Hauptfunktionen
	•	Multi-Agenten-Simulation
	•	Räuber-Beute-Dynamiken (Lotka-Volterra, Viren/Bakterien)
	•	Agenten mit Energie, Fähigkeiten, Neugier, Mutation & Selektion
	•	Evolutionärer Algorithmus zur Anpassung der Population
	•	Sensitivitätsanalyse mit Batch-Runs, Heatmap & 3D-Surface-Plots
	•	Automatische Berichtserstellung (HTML & PDF)
	•	ML-Vorhersagemodelle (z. B. Random Forest)
	•	Interaktive Visualisierung (Streamlit)
	•	Docker-Support
	•	Erweiterbare Analyse- und Plot-Tools

⸻
Struktur

```plaintext
.
├── __pycache__                          # Python Bytecode Cache
│   ├── ml_predictor.cpython-313.pyc
│   ├── report_engine.cpython-312.pyc
│   ├── report_engine.cpython-313.pyc
│   ├── sensitivity_engine.cpython-312.pyc
│   └── sensitivity_engine.cpython-313.pyc
├── agent_ecosystem                      # Multi-Agenten-Ökosystem-Simulator
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── agent.cpython-313.pyc
│   │   ├── config.cpython-313.pyc
│   │   ├── environment.cpython-313.pyc
│   │   └── simulator.cpython-313.pyc
│   ├── agent.py                         # Agenten-Logik
│   ├── config.py                        # Parameter & Einstellungen
│   ├── environment.py                   # Umweltsimulation
│   └── simulator.py                     # Simulations-Engine
├── app.py                               # Haupt-Startpunkt der App
├── assets                               # UI-Assets (Bilder, Stylesheets)
│   ├── 285025A1-F8EF-4200-B514-BE974E1B70E3_1_105_c.jpeg
│   ├── icon.png
│   └── style.css
├── avatar.png                           # Benutzer-Avatar/Icon
├── Dockerfile                           # Docker-Konfiguration
├── HANDBUCH                             # Projektdokumentation
│   ├
│   ├── Dual Layer Architecture for Data Driven Ecology.docx
│   └── Eco Simulator 2_Allgemein.pdf
├── ml_predictor.py                      # Maschinelles Lernen – Vorhersagemodul
├── models                               # (Platzhalter für ML/Datenmodelle)
├── predator_prey_sim                    # Räuber-Beute-Simulator
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── __init__.cpython-313.pyc
│   │   ├── config.cpython-312.pyc
│   │   ├── config.cpython-313.pyc
│   │   ├── integrators.cpython-312.pyc
│   │   ├── integrators.cpython-313.pyc
│   │   ├── simulator.cpython-312.pyc
│   │   ├── simulator.cpython-313.pyc
│   │   ├── visualizer.cpython-312.pyc
│   │   └── visualizer.cpython-313.pyc
│   ├── config.py                        # Parameter & Einstellungen
│   ├── integrators.py                   # Mathematische Integratoren
│   ├── simulator.py                     # Simulations-Engine
│   └── visualizer.py                    # Visualisierung
├── pyproject.toml                       # Projektkonfiguration & Abhängigkeiten
├── README.md                            # Hauptdokumentation
├── report_engine_agents.py              # Reportgenerator (Agenten-Simulation)
├── report_engine.py                     # Allgemeiner Reportgenerator
├── requirements.txt                     # Python-Abhängigkeiten
├── sensitivity_engine.py                # Sensitivitätsanalyse-Engine
├── sensitivity_report                   # Stylesheet für Sensitivitätsberichte
│   └── style.css
├── sensitivity_results                  # CSV-Dateien mit Analyseergebnissen
│   ├── results_0.02_0.005_0.1.csv
│   ├── results_0.03_0.007_0.15.csv
│   ├── results_0.04_0.006_0.25.csv
│   ├── results_0.05_0.009_0.2.csv
│   ├── results_alpha_0.18_beta_0.015_curiosity_0.5_mutation_rate_0.03_phi_0.005.csv
│   ├── results_alpha_0.22_beta_0.018_curiosity_0.6_mutation_rate_0.04_phi_0.006.csv
│   ├── results_alpha_0.25_beta_0.02_curiosity_0.4_mutation_rate_0.05_phi_0.005.csv
│   └── results_alpha_0.3_beta_0.022_curiosity_0.7_mutation_rate_0.06_phi_0.007.csv
├── templates                            # HTML-Templates
│   └── report_template.html
├── tests                                # Testfälle
│   └── test_simulator.py
└── tools                               # Analyse- und Kontrolltools
    ├── __pycache__
    │   ├── analyze_results.cpython-312.pyc
    │   ├── analyze_results.cpython-313.pyc
    │   ├── recommend_params.cpython-312.pyc
    │   └── recommend_params.cpython-313.pyc
    ├── _init__.py
    ├── analyze_results.py               # Ergebnisanalyse
    ├── control_dashboard.py             # Simulations-Dashboard
    ├── full_analysis.py                 # Vollständige Analyse-Skripte
    ├── plot_results.py                  # Ergebnisplots
    ├── README.md
    ├── recommend_params.py              # Parametervorschläge
    └── run_sensitivity.py               # Sensitivitätstests

'''

⸻
Wichtige Befehle

| Funktion            | Befehl                              |
| ------------------- | ----------------------------------- |
| Start Streamlit     | `streamlit run app.py`              |
| Dashboard           | `python tools/control_dashboard.py` |
| Vollanalyse         | `python tools/full_analysis.py`     |
| Sensitivitätstest   | `python tools/run_sensitivity.py`   |
| Analyse             | `python tools/analyze_results.py`   |
| Plot-Erstellung     | `python tools/plot_results.py`      |
| Parametervorschläge | `python tools/recommend_params.py`  |
| Tests               | `pytest tests/`                     |



⸻

Besondere Merkmale
	•	Streamlit-Visualisierung vollständig integriert
	•	Agentenevolution: Energie, Neugier, Mutation, Selektion
	•	ML-Prognose: Random Forest
	•	Erweiterte Sensitivitätsanalyse mit Heatmap und 3D-Surface-Plot
	•	Batch-Run & Berichtserstellung mit vollständigen Befehlen
	•	Notebooks für explorative Entwicklung
	•	Docker-Deployment (Port 8501 vorkonfiguriert)
	•	Modular & erweiterbar für zukünftige KI-Agenten & neue Umweltdynamiken

⸻

Zusammenfassung

eco_simulator stellt eine umfassende Plattform für simulationsbasierte ökologische Modellierung bereit.
Die Kombination aus agentenbasierten Algorithmen, ML, Sensitivitätsanalysen und moderner Visualisierung macht es zu einem leistungsfähigen Werkzeug für Forschung und angewandte KI.

⸻
