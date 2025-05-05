##config.py##

from dataclasses import dataclass

@dataclass
class SimulationConfig:
    alpha: float = 0.1
    beta: float = 0.02
    phi: float = 0.005
    delta: float = 0.01
    gamma: float = 0.1
    r_b: float = 0.5
    mu_b: float = 0.1
    k_ib: float = 0.05
    s_n: float = 1.0
    c_n: float = 0.1
    p_v: float = 0.3
    mu_v: float = 0.1
    k_iv: float = 0.05
    r_i: float = 0.2
    K_i: float = 50.0
    mu_i: float = 0.1

    initial_prey: float     = 40.0
    initial_predator: float = 9.0
    initial_bacteria: float = 10.0
    initial_virus: float    = 5.0
    initial_immune: float   = 1.0
    initial_nutrient: float = 100.0

    time_steps: int    = 300
    dt: float          = 0.1
    integrator: str    = "rk4"
    show_progress: bool = False

    # Erweiterte Parameter (werden ggf. ignoriert, aber erlaubt)
    mutation_rate: float = 0.0
    curiosity: float = 0.0
