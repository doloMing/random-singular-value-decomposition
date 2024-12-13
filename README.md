# Random SVD Principle and CMake Usage Guide

## 1. Random SVD Principle

### 1.1 Overview

Random Singular Value Decomposition (Random SVD) is a dimensionality reduction technique used for high-dimensional data. It approximates the singular value decomposition of a matrix through random projections, making it effective for handling large-scale datasets.

### 1.2 Mathematical Principle

Given a matrix \( A \in \mathbb{R}^{m \times n} \), its Singular Value Decomposition (SVD) can be expressed as:

\[
A = U \Sigma V^T
\]

where:
- \( U \) is an \( m \times m \) orthogonal matrix containing the left singular vectors.
- \( \Sigma \) is an \( m \times n \) diagonal matrix containing the singular values.
- \( V \) is an \( n \times n \) orthogonal matrix containing the right singular vectors.

### 1.3 Random Projection

The core idea of Random SVD is to reduce computational complexity through random projection. The specific steps are as follows:

1. **Generate a Random Matrix**: Generate a random matrix \( \Omega \in \mathbb{R}^{n \times k} \), where \( k \) is the desired number of features.

2. **Compute Projection**: Compute \( Y = A \Omega \), resulting in a smaller matrix \( Y \in \mathbb{R}^{m \times k} \).

3. **QR Decomposition**: Perform QR decomposition on \( Y \) to obtain the orthogonal matrix \( Q \) and the upper triangular matrix \( R \):

\[
Y = QR
\]

4. **Compute Matrix B**: Compute \( B = Q^T A \), and then perform SVD on \( B \):

\[
B = U_B \Sigma_B V_B^T
\]

5. **Recover U Matrix**: Finally, the left singular vectors \( U \) can be obtained as \( U = Q U_B \).

### 1.4 Summary of Formulas

The steps of Random SVD can be summarized as:

\[
Y = A \Omega
\]
\[
Q, R = \text{QR}(Y)
\]
\[
B = Q^T A
\]
\[
B = U_B \Sigma_B V_B^T
\]
\[
U = Q U_B
\]

## 2. CMake Usage Guide

### 2.1 Download CMake

1. Visit the [CMake official website](https://cmake.org/download/).
2. Choose the appropriate installation package for your operating system.
3. Follow the installation wizard to complete the installation.

### 2.2 Modify CMakeLists.txt

Create or modify the `CMakeLists.txt` file in the project root directory with the following content:


### 2.3 Compile Files Using CMake

1. Open a terminal (command prompt or terminal).
2. Navigate to the project root directory.
3. Create a build directory:

   ```bash
   mkdir build
   cd build
   ```

4. Run CMake to generate build files:

   ```bash
   cmake ..
   ```

5. Compile the project:

   ```bash
   cmake --build .
   ```

### 2.4 Run Tests

1. In the build directory, find random_svd.dll and load it via Python. Then, run the test file:

   ```bash
   python test.py
   ```

2. Check the output to ensure the program runs correctly.

## 3. Conclusion

Through the above steps, you can understand the principles of Random SVD based on its C++ version. Random SVD is an efficient dimensionality reduction technique suitable for handling large-scale datasets. 
