# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np
from .function import Solver

class _LinearRegression:
    def __init__(self, xdata, ydata):
        self.xdata = np.array(xdata)
        self.ydata = np.array(ydata)
        self.n = len(xdata)

    def __call__(self, xs: np.ndarray) -> float:
        """ Negative log likelihood of linear regression with Gaussian noise N(0,sigma)

        y = ax + b

        example:
        trained by xdata = [1, 2, 3, 4, 5, 6] and ydata = [1, 3, 2, 4, 3, 5].

        Model parameters (a, b, sigma) are corresponding to xs as the following,
        a = xs[0], b = xs[1], log(sigma**2) = xs[2]

        It has a global minimum f(xs) = 1.005071.. at
        xs = [0.628571..., 0.8, -0.664976...].    
        """
        assert xs.shape[0] == 3, f"ERROR: regression expects d=3 input, but receives d={xs.shape[0]} one"

        a, b, w = xs
        return 0.5 * (self.n * w + np.sum((a * self.xdata + b - self.ydata) ** 2) / np.exp(w))

class LinearRegression(Solver):
    def __init__(self, info, xdata, ydata):
        super().__init__(info)
        self.set_function(_LinearRegression(xdata, ydata))
