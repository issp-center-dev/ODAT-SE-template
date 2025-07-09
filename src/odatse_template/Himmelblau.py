# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np
from .function import Solver

def himmelblau(xs: np.ndarray) -> float:
    """Himmelblau's function

    It has four global minima f(xs) = 0 at
    xs=[3,2], [-2.805118..., 3.131312...], [-3.779310..., -3.2831860], and [3.584428..., -1.848126...].
    """
    assert xs.shape[0] == 2, f"ERROR: himmelblau expects d=2 input, but receives d={xs.shape[0]} one"
    x, y = xs
    return (x ** 2 + y - 11.0) ** 2 + (x + y ** 2 - 7.0) ** 2

class Himmelblau(Solver):
    def __init__(self, info):
        super().__init__(info, fn=himmelblau)
