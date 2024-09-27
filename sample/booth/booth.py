import numpy as np
import odatse.extra.template

class Booth(odatse.extra.template.Solver):
    def evaluate(self, xs: np.ndarray, args=()):
        assert xs.shape[0] == 2
        x, y = xs
        fx = (x + 2 * y - 7)**2 + (2 * x + y - 5)**2
        return fx
