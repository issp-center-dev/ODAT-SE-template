# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np
from .function import Solver

def ackley(xs: np.ndarray) -> float:
    """Ackley's function in arbitrary dimension

    It has one global minimum f(xs)=0 at xs=[0,0,...,0].
    It has many local minima.
    """
    a = np.mean(xs ** 2)
    a = 20 * np.exp(-0.2 * np.sqrt(a))
    b = np.cos(2.0 * np.pi * xs)
    b = np.exp(0.5 * np.sum(b))
    return 20.0 + np.exp(1.0) - a - b

class Ackley(Solver):
    def __init__(self, info):
        super().__init__(info, fn=ackley)
