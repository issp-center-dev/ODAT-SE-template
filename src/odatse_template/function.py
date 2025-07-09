# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import numpy as np
import odatse

# type hints
from pathlib import Path
from typing import Callable, Optional, Dict, Tuple


class Solver(odatse.solver.SolverBase):
    _func: Optional[Callable[[np.ndarray], float]]

    def __init__(self,
                 info: Optional[odatse.Info] = None,
                 fn: Optional[Callable[[np.ndarray], float]] = None) -> None:
        """
        Initialize the solver.

        Parameters
        ----------
        info: Info
        fn: callable object
        """
        self._name = "function"
        self._func = fn

    def evaluate(self, x: np.ndarray, args = (), nprocs: int = 1, nthreads: int = 1) -> float:
        if self._func is None:
            raise RuntimeError("ERROR: function is not set. Make sure that `set_function` is called.")
        return self._func(x)

    def set_function(self, f: Callable[[np.ndarray], float]) -> None:
        self._func = f
