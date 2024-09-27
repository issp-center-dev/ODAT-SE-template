import numpy as np

import odatse
import odatse.algorithm.mapper_mpi as mapper
import odatse.extra.template as function

info = odatse.Info.from_file("input.toml")
solver = function.Himmelblau(info)
runner = odatse.Runner(solver, info)

alg = mapper.Algorithm(info, runner)
alg.main()
