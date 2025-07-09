# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np
from .function import Solver

def rosenbrock(xs: np.ndarray) -> float:
    """Rosenbrock's function

    It has one global minimum f(xs) = 0 at xs=[1,1,...,1].
    """
    return np.sum(100.0 * (xs[1:] - xs[:-1] ** 2) ** 2 + (1.0 - xs[:-1]) ** 2)

class Rosenbrock(Solver):
    def __init__(self, info):
        super().__init__(info, fn=rosenbrock)
