# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np
import odatse_template

class Booth(odatse_template.Solver):
    def evaluate(self, xs: np.ndarray, args=()):
        assert xs.shape[0] == 2
        x, y = xs
        fx = (x + 2 * y - 7)**2 + (2 * x + y - 5)**2
        return fx
