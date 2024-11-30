# Random SVD Configuration and Testing Guide

## Overview


This guide provides instructions for configuring and testing the Random SVD implementations in C, C++, and Fortran. The implementations will be tested using a Python script (`test.py`).


## Prerequisites

Before proceeding, ensure you have the following installed on your system:

- **C/C++ Compiler**: GCC or any compatible compiler.

- **Fortran Compiler**: GFortran or any compatible Fortran compiler.

- **Python**: Version 3.x.


- **NumPy**: Install via pip:
  ```bash
  pip install numpy
  ```
- **SciPy**: Install via pip:
  ```bash
  pip install scipy
  ```
- **LAPACK and BLAS**: These libraries are required for linear algebra operations. You can install them as follows:

  - **Windows**: Use [OpenBLAS](https://www.openblas.net/) or [LAPACKe](http://www.netlib.org/lapack/).

  - **Linux**: Install via package manager: 
  ```bash
   sudo apt-get install liblapack-dev libblas-dev
  ```

  - **macOS**: Use Homebrew:
  ```bash
   brew install openblas
  ```
