import random
import numpy as np
from .config import AgentSimConfig

class Agent:
    __slots__ = ("x", "y", "speed", "sight", "strength", "camouflage", "curiosity",
                 "energy", "age", "config")

    def __init__(self, x: int, y: int, config: AgentSimConfig,
                 speed=1.0, sight=3, strength=1.0, camouflage=0.0, curiosity=0.5,
                 energy: float = None):
        self.x = x
        self.y = y
        self.config = config
        self.speed = speed
        self.sight = sight
        self.strength = strength
        self.camouflage = camouflage
        self.curiosity = curiosity
        self.energy = energy if energy is not None else config.energy_gain * 2
        self.age = 0

    def perceive(self, env) -> list[tuple[int, int]]:
        coords = []
        gs = self.config.grid_size
        # Fehler gefixt: dx und dy getrennt, sight in int() umgewandelt
        for dx in range(-int(self.sight), int(self.sight) + 1):
            for dy in range(-int(self.sight), int(self.sight) + 1):
                nx, ny = (self.x + dx) % gs, (self.y + dy) % gs
                if env.resources[nx, ny] > 0:
                    coords.append((nx, ny))
        return coords

    def decide_move(self, resources: list[tuple[int, int]]) -> tuple[int, int]:
        gs = self.config.grid_size
        if resources and random.random() > self.curiosity:
            tx, ty = min(resources, key=lambda c: abs(c[0] - self.x) + abs(c[1] - self.y))
        else:
            angle = random.random() * 2 * np.pi
            dx = int(round(np.cos(angle) * self.speed))
            dy = int(round(np.sin(angle) * self.speed))
            tx = (self.x + dx) % gs
            ty = (self.y + dy) % gs
        return tx, ty

    def move(self, tx: int, ty: int):
        self.x, self.y = tx, ty
        self.energy -= self.config.move_cost * self.speed

    def eat(self, env):
        gained = min(env.resources[self.x, self.y], self.config.energy_gain)
        env.resources[self.x, self.y] -= gained
        self.energy += gained * self.strength

    def reproduce(self) -> "Agent":
        child_attrs = {}
        for attr in ("speed", "sight", "strength", "camouflage", "curiosity"):
            val = getattr(self, attr)
            mutation = random.gauss(1.0, self.config.mutation_rate)
            child_attrs[attr] = max(0.0, val * mutation)
        self.energy /= 2
        return Agent(x=self.x, y=self.y, config=self.config, energy=self.energy, **child_attrs)

    def step(self, env) -> "Agent|None":
        self.age += 1
        if self.age > self.config.max_age or self.energy <= 0:
            return None
        resources = self.perceive(env)
        tx, ty = self.decide_move(resources)
        self.move(tx, ty)
        self.eat(env)
        if self.energy >= self.config.reproduction_threshold:
            return self.reproduce()
        return self