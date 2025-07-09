# SPDX-License-Identifier: MPL-2.0
#
# ODAT-SE-template -- Solver templates for open data analysis platform ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np

import odatse
#import odatse.algorithm.mapper_mpi as mapper
import odatse.algorithm.min_search as min_search
from odatse_template import LinearRegression
import odatse.domain

data = np.loadtxt("data.txt")

info = odatse.Info.from_file("input.toml")
solver = LinearRegression(info, xdata=data[:,0], ydata=data[:,1])
runner = odatse.Runner(solver, info)

region = odatse.domain.Region(param={"min_list": [-1,-1,-1], "max_list": [1,1,1]})

alg = min_search.Algorithm(info, runner, region)
alg.main()
