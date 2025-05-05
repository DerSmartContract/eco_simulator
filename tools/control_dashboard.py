import streamlit as st
from analyze_results import load_results
from recommend_params import suggest_changes
import pandas as pd
import plotly.express as px

# ------------------------- CONFIG & STYLE -------------------------
st.set_page_config(
    page_title="Ökosystem Kontrollzentrum",
    page_icon="🌱",
    layout="wide"
)

# Lade CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------------- HEADER -------------------------
st.title("🌱 Ökosystem Kontrollzentrum 2.0")

df = load_results()

if df.empty:
    st.warning("Keine Simulationsergebnisse gefunden.")
    st.stop()

# ------------------------- STATISTIKEN -------------------------
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Gesamt-Simulationen", len(df))
col2.metric("Kritisch", df[df["Stability"] == "Critical"].shape[0])
col3.metric("Durchschn. Beutepop.", f"{df['prey'].mean():.2f}" if "prey" in df else "N/A")
col4.metric("Durchschn. Mutation Rate", f"{df['mutation_rate'].mean():.3f}" if "mutation_rate" in df else "N/A")
col5.metric("Durchschn. Curiosity", f"{df['curiosity'].mean():.3f}" if "curiosity" in df else "N/A")

# ------------------------- KORRELATIONSMATRIX -------------------------
st.subheader("📊 Korrelation Heatmap")
corr = df.select_dtypes(include='number').corr()
fig = px.imshow(corr, text_auto=True, color_continuous_scale="viridis")
st.plotly_chart(fig, use_container_width=True)

# ------------------------- ERGEBNIS-TABELLE -------------------------
st.subheader("📋 Simulationsergebnisse")
st.dataframe(df)

# ------------------------- TRENDDIAGRAMM -------------------------
st.subheader("📈 Populations-Trends")
if "prey" in df and "alpha" in df:
    fig2 = px.scatter(df, x="alpha", y="prey", color="Stability",
                      size=df["predator"] if "predator" in df else None,
                      title="Beutepopulation vs. Alpha",
                      labels={"prey": "Beute", "alpha": "Alpha"})
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("Nicht genügend Daten für Populations-Trend-Diagramm.")

# ------------------------- TRENDDIAGRAMM Mutation -------------------------
st.subheader("🧬 Mutation Rate vs. Population")
if "mutation_rate" in df and "population" in df:
    fig3 = px.scatter(df, x="mutation_rate", y="population", color="Stability",
                      title="Mutation Rate vs. Population",
                      labels={"mutation_rate": "Mutation Rate", "population": "Population"})
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("Nicht genügend Daten für Mutations-Trend-Diagramm.")

# ------------------------- TRENDDIAGRAMM Curiosity -------------------------
st.subheader("🧠 Curiosity vs. Population")
if "curiosity" in df and "population" in df:
    fig4 = px.scatter(df, x="curiosity", y="population", color="Stability",
                      title="Curiosity vs. Population",
                      labels={"curiosity": "Curiosity", "population": "Population"})
    st.plotly_chart(fig4, use_container_width=True)
else:
    st.info("Nicht genügend Daten für Curiosity-Trend-Diagramm.")

# ------------------------- EMPFEHLUNGEN -------------------------
st.subheader("🧠 Empfehlungen für Parameteranpassung")
for idx, row in df.iterrows():
    params = ", ".join(f"{k}={round(v,3)}" for k,v in row.items() if k in ["alpha","beta","phi","mutation_rate","curiosity"] and pd.notna(v))
    st.markdown(f"**{params} | Stabilität: {row['Stability']}**")
    recs = suggest_changes(row)
    if recs:
        for r in recs:
            st.success(f"👉 {r}")
    else:
        st.info("✅ Keine Änderungen nötig.")
    st.divider()

# ------------------------- TICKER -------------------------
st.sidebar.header("🔔 System-Ticker")
if (df["Stability"] == "Critical").any():
    st.sidebar.error("⚠️ Kritische Simulationen erkannt.")
elif (df["Stability"] == "Unstable").any():
    st.sidebar.warning("⚠ Einige Instabilitäten festgestellt.")
else:
    st.sidebar.success("✅ Alle Simulationen stabil.")

# ------------------------- DOWNLOAD -------------------------
st.sidebar.download_button(
    label="📥 Ergebnisse als CSV",
    data=df.to_csv(index=False),
    file_name="simulationsergebnisse.csv",
    mime="text/csv"
)