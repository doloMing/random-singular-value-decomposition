import numpy as np
import ctypes
import time
import tracemalloc

# Load the shared library using a relative path
lib = ctypes.CDLL('./build/Debug/random_svd.dll')

# Check if the function exists
try:
    random_svd_func = getattr(lib, 'random_svd')
    print("Function 'random_svd' is available in the library.")
except AttributeError:
    print("Function 'random_svd' is not found in the library.")

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

# C++ random SVD wrapper
def test_random_svd_cpp(A, k):
    U = np.zeros((A.shape[0], k), dtype=np.float64)
    S = np.zeros((k, k), dtype=np.float64)
    V = np.zeros((A.shape[1], k), dtype=np.float64)

    # Call the C++ function
    lib.random_svd(A, A.shape[0], A.shape[1], U, S, V, k)

    return U, S, V

# Standard SVD
def test_standard_svd(A, k):
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    return U[:, :k], np.diag(S[:k]), Vt[:k, :]

# Python version of random SVD
def test_random_svd_python(A, k):
    m, n = A.shape
    Omega = np.random.randn(n, k)  # Random Gaussian matrix
    Y = A @ Omega  # A * Omega

    # QR decomposition
    Q, _ = np.linalg.qr(Y)

    # Compute B = Q^T * A
    B = Q.T @ A

    # SVD of B
    U, S, Vt = np.linalg.svd(B, full_matrices=False)
    U = Q @ U[:, :k]
    S = np.diag(S[:k])
    V = Vt[:k, :]

    return U, S, V

# Main function to compare results
def compare_svd_methods(k):
    # Generate a random matrix
    A = np.random.rand(300, 400).astype(np.float64)

    # Measure memory usage and time for C++ SVD
    tracemalloc.start()
    start_cpp = time.time()
    U_cpp, S_cpp, V_cpp = test_random_svd_cpp(A, k)
    end_cpp = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    cpp_memory = peak / 10**6  # Convert to MB

    # Measure memory usage and time for standard SVD
    tracemalloc.start()
    start_std = time.time()
    U_std, S_std, V_std = test_standard_svd(A, k)
    end_std = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    std_memory = peak / 10**6  # Convert to MB

    # Measure memory usage and time for Python random SVD
    tracemalloc.start()
    start_py_random = time.time()
    U_py, S_py, V_py = test_random_svd_python(A, k)
    end_py_random = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    py_random_memory = peak / 10**6  # Convert to MB

    # Calculate the error
    U_error_cpp = np.linalg.norm(U_cpp - U_std)
    S_error_cpp = np.linalg.norm(S_cpp - S_std)
    V_error_cpp = np.linalg.norm(V_cpp - V_std.T)

    U_error_py = np.linalg.norm(U_py - U_std)
    S_error_py = np.linalg.norm(S_py - S_std)
    V_error_py = np.linalg.norm(V_py - V_std)  # Transpose V_py for comparison

    # Print results
    print(f"K = {k}:")
    print("C++ SVD Time: {:.6f} seconds, Memory: {:.6f} MB".format(end_cpp - start_cpp, cpp_memory))
    print("Standard SVD Time: {:.6f} seconds, Memory: {:.6f} MB".format(end_std - start_std, std_memory))
    print("Python Random SVD Time: {:.6f} seconds, Memory: {:.6f} MB".format(end_py_random - start_py_random, py_random_memory))
    print("U Error (C++ vs Standard): {:.6f}".format(U_error_cpp))
    print("S Error (C++ vs Standard): {:.6f}".format(S_error_cpp))
    print("V Error (C++ vs Standard): {:.6f}".format(V_error_cpp))
    print("U Error (Python Random vs Standard): {:.6f}".format(U_error_py))
    print("S Error (Python Random vs Standard): {:.6f}".format(S_error_py))
    print("V Error (Python Random vs Standard): {:.6f}".format(V_error_py))
    print("-" * 40)

# Run the comparison for different values of k
for k in [5, 10, 50, 100, 200]:
    compare_svd_methods(k)
