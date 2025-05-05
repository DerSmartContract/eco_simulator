import streamlit as st
import numpy as np
from predator_prey_sim.simulator import Simulator as PpSimulator
from predator_prey_sim.config import SimulationConfig as PpConfig
from predator_prey_sim.visualizer import plot_time_series as plot_pp_series
import report_engine
import ml_predictor
from agent_ecosystem.config import AgentSimConfig
from agent_ecosystem.simulator import AgentSimulator
import plotly.graph_objects as go

st.set_page_config(page_title="Ökosystem Live-Simulator 2.0", page_icon="🧬", layout="wide")
st.image("avatar.png", width=150)
st.title("Echtzeit Ökosystem Simulator 2.0")

tabs = st.tabs(["Predator-Prey", "Agenten-basierte Evolution"])

with tabs[0]:
    alpha = st.slider("Beute-Wachstumsrate (α)", 0.01, 0.5, 0.1)
    beta  = st.slider("Räuber-Fressrate (β)", 0.001, 0.1, 0.02)
    phi   = st.slider("Virus-Infektionsrate (φ)", 0.001, 0.01, 0.005)
    initial_prey     = st.slider("Anfangs-Beute", 10, 100, 40)
    initial_predator = st.slider("Anfangs-Räuber", 1, 20, 9)

    if st.button("Simulation starten", key="pp_sim"):
        cfg = PpConfig(
            alpha=alpha, beta=beta, phi=phi,
            initial_prey=initial_prey,
            initial_predator=initial_predator,
            time_steps=300, dt=0.1,
            integrator="rk4", show_progress=False
        )
        sim = PpSimulator(cfg)
        results = sim.run()
        st.success("Simulation abgeschlossen")
        plot_pp_series(results, backend="plotly")

    if st.button("PDF-Bericht generieren", key="pp_report"):
        report_engine.generate_report()
        st.success("Bericht erstellt: sensitivity_report/report.pdf")

    if st.button("ML-Vorhersage anzeigen", key="pp_ml"):
        pred = ml_predictor.predict(alpha, beta, phi)
        st.info(f"ML-Vorhersage – Virus-Endpopulation: {pred:.2f}")

with tabs[1]:
    init_agents = st.slider("Start-Population", 5, 100, 20)
    grid_size   = st.slider("Grid-Größe", 20, 100, 50)
    steps       = st.slider("Zeitschritte", 100, 1000, 500)
    mut_rate    = st.slider("Mutationsrate", 0.0, 0.2, 0.05)
    repro_thr   = st.slider("Reproduktions-Energie", 50, 200, 120)
    regen       = st.slider("Resource Regen", 0.1, 5.0, 1.0)

    if st.button("Agenten-Simulation starten", key="agent_sim"):
        cfg = AgentSimConfig(
            initial_agents=init_agents,
            grid_size=grid_size,
            time_steps=steps,
            mutation_rate=mut_rate,
            reproduction_threshold=repro_thr,
            resource_regen=regen
        )
        sim = AgentSimulator(cfg)
        res = sim.run()
        st.success("Simulation abgeschlossen!")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=res["time"], y=res["population"], name="Pop."))
        fig.add_trace(go.Scatter(x=res["time"], y=res["avg_speed"], name="Ø Speed"))
        fig.add_trace(go.Scatter(x=res["time"], y=res["avg_curiosity"], name="Ø Curiosity"))
        fig.update_layout(xaxis_title="Zeit", yaxis_title="Wert")
        st.plotly_chart(fig)
