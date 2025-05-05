from typing import Protocol, Callable
import numpy as np
from scipy.integrate import solve_ivp

class Integrator(Protocol):
    def step(self, f: Callable[[np.ndarray], np.ndarray],
             y: np.ndarray, dt: float) -> np.ndarray: ...

class Euler:
    def step(self, f, y, dt):
        return y + dt * f(y)

class RK4:
    def step(self, f, y, dt):
        k1 = f(y)
        k2 = f(y + 0.5 * dt * k1)
        k3 = f(y + 0.5 * dt * k2)
        k4 = f(y + dt * k3)
        return y + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)

class SciPyRK45:
    def step(self, f, y, dt):
        sol = solve_ivp(lambda t, s: f(s), (0, dt), y,
                        method="RK45", t_eval=[dt])
        return sol.y[:, -1]

_INTEGRATORS = {
    "euler": Euler,
    "rk4": RK4,
    "scipy_rk45": SciPyRK45,
}

def get_integrator(name: str) -> Integrator:
    try:
        return _INTEGRATORS[name]()
    except KeyError as e:
        raise ValueError(f"Unbekannter Integrator: {name}") from e
