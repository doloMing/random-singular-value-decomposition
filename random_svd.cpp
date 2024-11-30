// random_svd.cpp
#include <iostream>
#include <Eigen/Dense>

using namespace Eigen;

void randomSVD(const MatrixXd& A, MatrixXd& U, MatrixXd& S, MatrixXd& V, int k) {
    // Random projection
    MatrixXd Omega = MatrixXd::Random(A.cols(), k);
    MatrixXd Y = A * Omega;

    // QR decomposition
    HouseholderQR<MatrixXd> qr(Y);
    MatrixXd Q = qr.householderQ();

    // Compute B = Q^T * A
    MatrixXd B = Q.transpose() * A;

    // SVD of B
    JacobiSVD<MatrixXd> svd(B, ComputeThinU | ComputeThinV);
    U = Q * svd.matrixU();
    S = svd.singularValues().asDiagonal();
    V = svd.matrixV();
}

extern "C" {
    void random_svd(double* A, int rows, int cols, double* U, double* S, double* V, int k) {
        MatrixXd matA = Map<MatrixXd>(A, rows, cols);
        MatrixXd matU, matS, matV;
        randomSVD(matA, matU, matS, matV, k);
        
        // Copy results back to output arrays
        Map<MatrixXd>(U, rows, k) = matU;
        Map<MatrixXd>(S, k, k) = matS;
        Map<MatrixXd>(V, cols, k) = matV;
    }
}
