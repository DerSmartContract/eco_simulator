##simulator.py##
import numpy as np
from .config import AgentSimConfig
from .environment import Environment
from .agent import Agent

class AgentSimulator:
    def __init__(self, config: AgentSimConfig):
        self.cfg = config
        self.env = Environment(config)
        self.agents: list[Agent] = []
        gs = config.grid_size
        # Agents übernehmen anfängliche curiosity aus der Config, mutation_rate wird intern genutzt.
        for _ in range(config.initial_agents):
            x, y = np.random.randint(gs), np.random.randint(gs)
            self.agents.append(Agent(
                x, y, config,
                curiosity=config.curiosity  # setzt Start-Curiosity aus der Config
            ))

    def run(self) -> dict[str, np.ndarray]:
        times = np.arange(self.cfg.time_steps)
        pop  = np.zeros_like(times, dtype=int)
        avg_speed   = np.zeros_like(times, dtype=float)
        avg_curio   = np.zeros_like(times, dtype=float)

        for t in times:
            self.env.regenerate()
            new_agents = []
            for agent in self.agents:
                result = agent.step(self.env)
                if isinstance(result, Agent) and result is not agent:
                    new_agents.append(result)
                if result:
                    new_agents.append(agent)
            self.agents = new_agents
            pop[t] = len(self.agents)
            if self.agents:
                avg_speed[t] = np.mean([a.speed for a in self.agents])
                avg_curio[t] = np.mean([a.curiosity for a in self.agents])

        return {
            "time": times,
            "population": pop,
            "avg_speed": avg_speed,
            "avg_curiosity": avg_curio
        }
