# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np

import odatse
import odatse.algorithm.min_search as min_search
from booth import Booth

info = odatse.Info.from_file("input.toml")
solver = Booth(info)
runner = odatse.Runner(solver, info)

alg = min_search.Algorithm(info, runner)
alg.main()
