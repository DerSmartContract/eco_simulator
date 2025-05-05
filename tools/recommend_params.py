##recommend_params.py##



def suggest_changes(row):
    suggestions = []
    # Predator-Prey Logik
    if "virus" in row:
        if row["virus"] > 50:
            suggestions.append("Phi senken (weniger Virusinfektion)")
        if row.get("prey", 0) < 5:
            suggestions.append("Alpha erhöhen (mehr Beutewachstum)")
        if row.get("predator", 0) < 3:
            suggestions.append("Beta verringern (weniger Räuber-Fressrate)")

    # Agenten-System Logik
    if "population" in row:
        if row["population"] < 5:
            suggestions.append("Mutation_rate leicht erhöhen (um Anpassung zu fördern)")
        if row["population"] > 50:
            suggestions.append("Mutation_rate senken (um Stabilität zu fördern)")

    if "avg_curiosity" in row:
        if row["avg_curiosity"] < 0.3:
            suggestions.append("Curiosity erhöhen (mehr Erkundung)")
        elif row["avg_curiosity"] > 0.8:
            suggestions.append("Curiosity senken (zu hohe Erkundung kann Energie kosten)")

    return suggestions

if __name__ == "__main__":
    from analyze_results import load_results
    df = load_results()

    for idx, row in df.iterrows():
        param_display = ", ".join(
            f"{k}={v}"
            for k, v in row.items()
            if k in ["alpha", "beta", "phi", "mutation_rate", "curiosity"]
        )
        print(f"Parameterkombination: {param_display}")
        print("Stabilität:", row["Stability"])
        recs = suggest_changes(row)
        if recs:
            print("Empfehlungen:")
            for rec in recs:
                print(" -", rec)
        else:
            print("Keine Änderungen empfohlen.")
        print("-" * 40)