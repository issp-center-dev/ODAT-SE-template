Minimization of Himmelblau function
================================================================

In this tutorial, we will write a user program using ODAT-SE-template module and perform analyese. As an example, we adopt the Nelder-Mead method for the inverse problem algorithm.


Location of the sample files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample files are located in ``sample/himmelblau``.
The following files are stored in the folder.

- ``main.py``

  Source file of the main program. This program reads ``input.toml`` for the parameters.

- ``input.toml``

  Input parameter file for ``main.py``.

- ``do.sh``

  Script file for running this tutorial.

- ``plot_colormap_2d.py``

  Program for visualizing the results.

The following sections describe these files and then show the actual calculation results.


Description of main program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``main.py`` is a simple program for the analyses using ODAT-SE-template module.
The entire source file is shown as follows:

.. code-block:: python

    import numpy as np

    import odatse
    import odatse.algorithm.mapper_mpi as mapper
    from odatse.extra.template import Himmelblau

    info = odatse.Info.from_file("input.toml")
    solver = Himmelblau(info)
    runner = odatse.Runner(solver, info)

    alg = mapper.Algorithm(info, runner)
    alg.main()


At the beginning of the program, the required modules are imported as listed below.

- ``odatse`` for the main module of ODAT-SE.

- ``odatse.algorithm.mapper_mpi`` for the module of the inverse problem algorithm.

- ``Himmelblau`` class from ``odatse.extra.template`` module.

Next, the instances of the classes are created.

- ``odatse.Info`` class

  This class is for storing the parameters.
  An instance is created by calling a class method ``from_file`` with a path to TOML file as an argument.

- ``Himmelblau`` class

  This class is for the Himmelblau function defined in the ODAT-SE-template module.
  An instance is created by passing an instance of Info class.

- ``odatse.Runner`` class

  This class is for connecting the direct problem solver and the inverse problem algorithm.
  An instance is created by passing an instance of Solver class and an instance of Info class.

- ``odatse.algorithm.min_search.Algorithm`` class

  This class is for the inverse problem algorithm.
  In this tutorial, we use ``min_search`` module that implements the optimization by Nelder-Mead method.
  An instance is created by passing an instance of Runner class.

After creating the instances of Solver, Runner, and Algorithm in this order, we invoke ``main()`` method of the Algorithm class to start analyses.


Input files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An example of the input parameter file ``input.toml`` is shown below.
Except, ``algorithm.name`` parameter for specifying the algorithm type should be ignored.

.. code-block:: toml

    [base]
    dimension = 2
    output_dir = "output"

    [algorithm]
    seed = 12345

    [algorithm.param]
    max_list = [6.0, 6.0]
    min_list = [-6.0, -6.0]
    num_list = [31, 31]

    [solver]

    [runner]
    [runner.log]
    interval = 20


Calculation execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, move to the folder where the sample files are located. (We assume that you are directly under the directory where you downloaded this software.)

.. code-block::

   $ cd sample/himmelblau

Run the main program. The computation time will take only a few seconds on a normal PC.

.. code-block::

   $ mpiexec -np 4 python3 main.py

In the above, the main program is executed with 4 MPI parallel processes.
The standard output will look as follows.

.. code-block::

    Make ColorMap
    Iteration : 1/240
    Iteration : 2/240
    Iteration : 3/240
    Iteration : 4/240
    Iteration : 5/240
    Iteration : 6/240
    Iteration : 7/240
    Iteration : 8/240
    Iteration : 9/240
    Iteration : 10/240
    ...


Visualization of results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By plotting ``output/ColorMap.txt``, you can identify the region of parameters in which the function yield small values.
A program to draw such a two-dimensional plot is prepared in ``plot_colormap_2d.py``.

.. code-block::

    $ python3 plot_colormap_2d.py

By typing as above, ``ColorMapFig.png`` is generated in which a color map of the function values evaluated at the grid, on top of the contour of Himmelblau function.

.. figure:: ../../../common/img/himmelblau_mapper.*

   A color map of the function values in the two-dimensional parameter space.
