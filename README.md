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

## File Structure

Create a directory for your project and place the following files inside it:

```
D:\Files\Computational Science\random SVD\
│
├── random_svd.c
├── random_svd.cpp
├── random_svd.f90
└── test.py
```

## Compilation Instructions

### 1. Compile the C Version

Open a command prompt and navigate to the directory containing `random_svd.c`. Use the following command to compile:

```bash
gcc -shared -o "random_svd.so" -fPIC "random_svd.c" -llapack -lblas
```

### 2. Compile the C++ Version

Use the following command to compile the C++ version:

```bash
g++ -shared -o "random_svd.so" -fPIC "random_svd.cpp" -I"path_to_eigen" -llapack -lblas
```

Make sure to replace `path_to_eigen` with the actual path to the Eigen library.

### 3. Compile the Fortran Version

Use the following command to compile the Fortran version:

```bash
gfortran -shared -o "random_svd.so" -fPIC "random_svd.f90"
```

## Running the Tests

After compiling the libraries, you can run the `test.py` script to test all three implementations:

```bash
python test.py
```

This will execute the tests for the C, C++, and Fortran versions of Random SVD and print the results.

## Conclusion

You have successfully configured and tested the Random SVD implementations in C, C++, and Fortran. If you encounter any issues, ensure that all paths are correctly set and that the necessary libraries are installed.
