# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

from .function import Solver

from .Quadratics import Quadratics
from .Quartics import Quartics
from .Ackley import Ackley
from .Rosenbrock import Rosenbrock
from .Himmelblau import Himmelblau
from .LinearRegression import LinearRegression
