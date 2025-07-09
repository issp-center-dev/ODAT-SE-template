# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np
from .function import Solver

def quartics(xs: np.ndarray) -> float:
    """quartic function with two minimum

    It has two global minimum f(xs)=0 at xs = [1,1,...,1] and [0,0,...,0].
    It has one suddle point f(0,0,...,0) = 1.0.
    """

    return np.mean((xs - 1.0) ** 2) * np.mean((xs + 1.0) ** 2)

class Quartics(Solver):
    def __init__(self, info):
        super().__init__(info, fn=quartics)
