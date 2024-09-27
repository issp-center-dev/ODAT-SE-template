import numpy as np

import odatse
import odatse.algorithm.mapper_mpi as mapper
from odatse.extra.template import Himmelblau

info = odatse.Info.from_file("input.toml")
solver = Himmelblau(info)
runner = odatse.Runner(solver, info)

alg = mapper.Algorithm(info, runner)
alg.main()
