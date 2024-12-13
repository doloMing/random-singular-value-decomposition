cmake_minimum_required(VERSION 3.1)
project(RandomSVD)

# Set the path for Eigen
set(EIGEN3_INCLUDE_DIR "D:/Files/CppLibs/eigen-3.3.9")
include_directories(${EIGEN3_INCLUDE_DIR})

# Create a shared library
add_library(random_svd SHARED "D:/Files/Computational_science/random_SVD/random_svd.cpp")  # Ensure the path is correct

# Optionally, set C++ standard
set_target_properties(random_svd PROPERTIES CXX_STANDARD 11)  # Adjust the C++ standard if needed