# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np

import odatse
import odatse.algorithm.mapper_mpi as mapper
from odatse_template import Himmelblau

info = odatse.Info.from_file("input.toml")
solver = Himmelblau(info)
runner = odatse.Runner(solver, info)

alg = mapper.Algorithm(info, runner)
alg.main()
