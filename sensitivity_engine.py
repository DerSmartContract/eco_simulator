##sensitivity_engine.py##

from multiprocessing import Pool
import pandas as pd
import os

def run_simulation(params):
    from predator_prey_sim.simulator import Simulator
    from predator_prey_sim.config import SimulationConfig
    cfg = SimulationConfig(**params)
    sim = Simulator(cfg)
    res = sim.run()
    df = pd.DataFrame(res)

    # Parameter als Spalten zum DataFrame hinzufügen
    for key, value in params.items():
        df[key] = value

    # Dynamischer Dateiname mit allen Parametern
    param_str = "_".join(f"{k}_{v}" for k, v in sorted(params.items()))
    fname = f"results_{param_str}.csv"
    path = os.path.join("sensitivity_results", fname)
    df.to_csv(path, index=False)
    return path

def batch_run(param_list, processes: int = None):
    os.makedirs("sensitivity_results", exist_ok=True)
    with Pool(processes) as pool:
        return pool.map(run_simulation, param_list)
