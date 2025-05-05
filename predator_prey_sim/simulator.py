##simulator.py##

import numpy as np
from .config import SimulationConfig
from .integrators import get_integrator

class Simulator:
    __slots__ = ("cfg", "integrator")

    def __init__(self, cfg: SimulationConfig):
        self.cfg = cfg
        self.integrator = get_integrator(cfg.integrator)
        # Hinweis: mutation_rate und curiosity werden akzeptiert,
        # haben aber in diesem Simulator keine Funktion.

    def _derivatives(self, state: np.ndarray) -> np.ndarray:
        prey, pred, bact, virus, immune, nut = state
        c = self.cfg

        # Schutz vor Division durch Null
        denom = c.K_i + bact + virus
        denom = denom if denom > 1e-8 else 1e-8

        return np.array([
            c.alpha * prey - c.beta * prey * pred,
            c.delta * prey * pred - c.gamma * pred,
            np.clip(c.r_b * bact * nut - c.mu_b * bact - c.phi * virus * bact - c.k_ib * immune * bact, -1e6, 1e6),
            np.clip(c.p_v * c.phi * virus * bact - c.mu_v * virus - c.k_iv * immune * virus, -1e6, 1e6),
            c.r_i * immune * (bact + virus) / denom - c.mu_i * immune,
            c.s_n - c.c_n * bact * nut
        ])

    def run(self) -> dict[str, np.ndarray]:
        n, dt = self.cfg.time_steps, self.cfg.dt
        data = np.zeros((n, 6))
        state = np.array([
            self.cfg.initial_prey,
            self.cfg.initial_predator,
            self.cfg.initial_bacteria,
            self.cfg.initial_virus,
            self.cfg.initial_immune,
            self.cfg.initial_nutrient
        ], dtype=float)

        for i in range(n):
            if np.any(~np.isfinite(state)):
                # Wenn ein Wert NaN oder inf ist, stoppen
                print(f"⚠ Instabilität bei Zeitschritt {i}. Simulation abgebrochen.")
                data = data[:i]  # Nur bis zu diesem Schritt speichern
                break

            data[i] = np.clip(state, 0.0, None)
            state = self.integrator.step(self._derivatives, state, dt)

            # Künstlicher Clamp zum Schutz
            state = np.clip(state, 0.0, 1e9)

        times = np.linspace(0, dt * (len(data) - 1), len(data))
        keys = ["time", "prey", "predator", "bacteria", "virus", "immune", "nutrient"]
        values = [times] + [data[:, j] for j in range(data.shape[1])]

        result = dict(zip(keys, values))

        # mutation_rate & curiosity für spätere Tools ergänzen
        result["mutation_rate"] = np.full_like(times, self.cfg.mutation_rate)
        result["curiosity"] = np.full_like(times, self.cfg.curiosity)

        return result