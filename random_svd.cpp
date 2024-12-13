#include <iostream>
#include <Eigen/Dense>
#include <random>

using namespace Eigen;

extern "C" {
    __declspec(dllexport) void randomSVD(const MatrixXd& A, MatrixXd& U, MatrixXd& S, MatrixXd& V, int k) noexcept {
        try {
            // Check if k is valid
            if (k <= 0 || k > std::min(A.rows(), A.cols())) {
                throw std::invalid_argument("k must be between 1 and min(rows, cols)");
            }

            // Print dimensions for debugging
            std::cout << "The dimensions of input matrix: " << A.rows() << " x " << A.cols() << std::endl;

            // Preallocate matrices
            U = MatrixXd::Zero(A.rows(), k);
            S = MatrixXd::Zero(k, k);
            V = MatrixXd::Zero(A.cols(), k);

            // Generate random matrix Omega
            MatrixXd Omega = MatrixXd::Random(A.cols(), k);
            MatrixXd Y = A * Omega;

            // QR decomposition
            HouseholderQR<MatrixXd> qr(Y);
            MatrixXd Q = qr.householderQ();

            // Compute B = Q^T * A
            MatrixXd B = Q.transpose() * A;

            // SVD of B
            JacobiSVD<MatrixXd> svd(B, ComputeThinU | ComputeThinV);
            U = Q * svd.matrixU().leftCols(k);
            S = svd.singularValues().head(k).asDiagonal();
            V = svd.matrixV().leftCols(k);

        } catch (const std::exception& e) {
            std::cerr << "Exception caught: " << e.what() << std::endl;
        } catch (...) {
            std::cerr << "Unknown exception caught." << std::endl;
        }
    }

    __declspec(dllexport) void random_svd(double* A, int rows, int cols, double* U, double* S, double* V, int k) {
        MatrixXd matA = Map<MatrixXd>(A, rows, cols);
        MatrixXd matU, matS, matV;

        // Initialize U, S, and V with the correct dimensions
        matU.resize(rows, k);
        matS.resize(k, k);
        matV.resize(cols, k);

        randomSVD(matA, matU, matS, matV, k);
        
        Map<MatrixXd>(U, rows, k) = matU;  // Output U
        Map<MatrixXd>(S, k, k) = matS;      // Output S
        Map<MatrixXd>(V, cols, k) = matV;   // Output V
    }
}
