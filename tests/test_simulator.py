import numpy as np
import pytest
from predator_prey_sim.config import SimulationConfig
from predator_prey_sim.simulator import Simulator

def test_derivative_non_negative():
    cfg = SimulationConfig(time_steps=10, dt=0.1)
    sim = Simulator(cfg)
    res = sim.run()
    assert np.all(res["time"] >= 0)
    for key in ["prey","predator","bacteria","virus","immune","nutrient"]:
        assert np.all(res[key] >= 0)
