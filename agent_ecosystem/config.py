##config.py##
from dataclasses import dataclass

@dataclass
class AgentSimConfig:
    grid_size: int = 50
    initial_agents: int = 20
    max_age: int = 100
    energy_gain: float = 20.0
    move_cost: float = 1.0
    reproduction_threshold: float = 120.0
    mutation_rate: float = 0.05
    resource_regen: float = 1.0
    max_resource: float = 5.0
    time_steps: int = 500
    alpha: float = 0.1
    curiosity: float = 0.5
