Installation of ODAT-SE-template
================================================================

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Python3 (>=3.6.8)

  - The following Python packages are required.

    - tomli >= 1.2
    - numpy >= 1.14

- ODAT-SE version 3.0 and later


How to download and install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install ODAT-SE

   - From source files:

     Download source files of ODAT-SE from the repository as follows:

     .. code-block:: bash

	$ git clone https://github.com/issp-center-dev/ODAT-SE.git

     Install ODAT-SE using ``pip`` command:

     .. code-block:: bash

	$ cd ODAT-SE
	$ python3 -m pip install .

     You may add ``--user`` option to install ODAT-SE locally (in ``$HOME/.local``).

     If you run the following command instead, optional packages will also be installed at the same time.

     .. code-block:: bash

	$ python3 -m pip install .[all]

2. Install ODAT-SE-template

   - From source files:

     The source files of ODAT-SE-template are available from the GitHub repository. After obtaining the source files, install ODAT-SE-template using ``pip`` command as follows:

     .. code-block:: bash

	$ git clone https://github.com/issp-center-dev/ODAT-SE-template.git
	$ cd ODAT-SE-template
	$ python3 -m pip install .

     You may add ``--user`` option to install the package locally (in ``$HOME/.local``).

     Then, the library of ODAT-SE-template wil be installed.


How to run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In ODAT-SE, the analysis is done by using a predefined optimization algorithm and a direct problem solver.
The ways to do analyses of functions is to write a program for the analysis with ODAT-SE-template library and ODAT-SE framework.
The type of the inverse problem algorithms can be chosen by importing the appropriate module.
A flexible use would be possible, for example, to include data generation within the program.
The types of parameters and the instruction to use the library will be given in the subsequent sections.


How to uninstall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In order to uninstall ODAT-SE-template and 2DMAT modules, type the following commands:

.. code-block:: bash

   $ python3 -m pip uninstall ODAT-SE-template ODAT-SE
