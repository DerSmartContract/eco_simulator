
# 📂 Eco Simulator – Projektstruktur & Kontextübersicht

## Struktur

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
```

##  Zusammenfassung

**Eco Simulator** ist ein modulares Simulations-Framework mit:
- **Agentenbasierten Ökosystemen** (agent_ecosystem)
- **Räuber-Beute-Dynamiken** (predator_prey_sim)
- **ML-Vorhersagemodul** (ml_predictor.py)
- **Sensitivitätsanalyse** (sensitivity_engine.py)
- **Visualisierung & Reporting** (tools/, report_engine.py, templates/)
- **Dokumentation & Ergebnisse** (HANDBUCH/, sensitivity_results/)


