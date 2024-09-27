import numpy as np

import odatse
#import odatse.algorithm.mapper_mpi as mapper
import odatse.algorithm.min_search as min_search
from odatse.extra.template import LinearRegression
import odatse.domain

data = np.loadtxt("data.txt")

info = odatse.Info.from_file("input.toml")
solver = LinearRegression(info, xdata=data[:,0], ydata=data[:,1])
runner = odatse.Runner(solver, info)

region = odatse.domain.Region(param={"min_list": [-1,-1,-1], "max_list": [1,1,1]})

alg = min_search.Algorithm(info, runner, region)
alg.main()
