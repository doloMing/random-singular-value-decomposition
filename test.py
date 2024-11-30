import numpy as np
import ctypes

## This is the .c version
# Load the shared library
lib = ctypes.CDLL('./random_svd.so')

# Define the function signature
lib.random_svd.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
    ctypes.c_int,
    ctypes.c_int,
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
    ctypes.c_int
]

# Example usage
def test_random_svd_c():
    A = np.random.rand(100, 50).astype(np.float64)
    U = np.zeros((100, 10), dtype=np.float64)
    S = np.zeros((10, 10), dtype=np.float64)
    V = np.zeros((50, 10), dtype=np.float64)

    lib.random_svd(A, A.shape[0], A.shape[1], U, S, V, 10)

    print("U:", U)
    print("S:", S)
    print("V:", V)

test_random_svd_c()


## This is the Fortran version
# Load the shared library
lib = ctypes.CDLL('./random_svd.so')

# Example usage
def test_random_svd_fortran():
    A = np.random.rand(100, 50).astype(np.float64)
    U = np.zeros((100, 10), dtype=np.float64)
    S = np.zeros((10, 10), dtype=np.float64)
    V = np.zeros((50, 10), dtype=np.float64)

    lib.random_svd(A, A.shape[0], A.shape[1], U, S, V, 10)

    print("U:", U)
    print("S:", S)
    print("V:", V)

test_random_svd_fortran()

## This is the .cpp version
# Load the shared library
lib = ctypes.CDLL('./random_svd.so')

# Define the function signature
lib.random_svd.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
                            ctypes.c_int,
                            ctypes.c_int,
                            np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
                            np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
                            np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),
                            ctypes.c_int]

# Example usage
def test_random_svd_cpp():
    A = np.random.rand(100, 50).astype(np.float64)
    U = np.zeros((100, 10), dtype=np.float64)
    S = np.zeros((10, 10), dtype=np.float64)
    V = np.zeros((50, 10), dtype=np.float64)

    lib.random_svd(A, A.shape[0], A.shape[1], U, S, V, 10)

    print("U:", U)
    print("S:", S)
    print("V:", V)

test_random_svd_cpp()
