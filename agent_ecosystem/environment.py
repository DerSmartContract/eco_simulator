import numpy as np
from .config import AgentSimConfig

class Environment:
    def __init__(self, config: AgentSimConfig):
        self.config = config
        gs = config.grid_size
        self.resources = np.full((gs, gs), config.max_resource / 2.0)

    def regenerate(self):
        self.resources += self.config.resource_regen
        np.clip(self.resources, 0, self.config.max_resource, out=self.resources)
