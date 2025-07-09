# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np
from .function import Solver

def quadratics(xs: np.ndarray) -> float:
    """quadratic (sphear) function

    It has one global miminum f(xs)=0 at xs = [0,0,...,0].
    """
    return np.sum(xs * xs)

class Quadratics(Solver):
    def __init__(self, info):
        super().__init__(info, fn=quadratics)
