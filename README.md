# ODAT-SE-template: templates for ODAT-SE solver modules

Open Data Analysis Tool for Science and Engineering (ODAT-SE) is an open platform for data analysis. It has been developed by the name 2DMAT, and since version 3.0 it is organized by modularizing direct problem solvers and search algorithms. This package provides solver modules for optimization problems of analytical functions, as templates for direct problem solvers of ODAT-SE.

### Prerequisites

- Required
  - Python >= 3.6.8
  - numpy >= 1.14
  - tomli >= 1.2.0
  - ODAT-SE >= 3.0

### Install

- From source
  1. install ODAT-SE package
    - git clone https://github.com/issp-center-dev/ODAT-SE.git
    - cd ODAT-SE
    - python3 -m pip install .[all]
  2. install ODAT-SE-template package
    - cd ODAT-SE-template
    - python3 -m pip install .

### Simple usage

- Prepare a python script (e.g. main.py) using ODAT-SE and ODAT-SE-template, and run the script by `python3 main.py`

- See the manual for details.

### License

This package is distributed under GNU General Public License version 3 (GPL v3) or later.

### Copyright

Copyright (c) 2024- The University of Tokyo. All rights reserved.*
This software was developed with the support of "*Project for advancement of software usability in materials science*" of The Institute for Solid State Physics, The University of Tokyo.

