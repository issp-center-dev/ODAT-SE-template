import numpy as np

import odatse
import odatse.algorithm.min_search as min_search
from booth import Booth

info = odatse.Info.from_file("input.toml")
solver = Booth(info)
runner = odatse.Runner(solver, info)

alg = min_search.Algorithm(info, runner)
alg.main()
