// random_svd.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <lapacke.h>
#include <cblas.h>

void random_svd(double* A, int rows, int cols, double* U, double* S, double* V, int k) {
    // Random projection
    double* Omega = (double*)malloc(cols * k * sizeof(double));
    for (int i = 0; i < cols * k; i++) {
        Omega[i] = ((double)rand() / RAND_MAX);
    }

    double* Y = (double*)malloc(rows * k * sizeof(double));
    cblas_dgemm(CblasColMajor, CblasNoTrans, CblasNoTrans, rows, k, cols, 1.0, A, rows, Omega, cols, 0.0, Y, rows);

    // QR decomposition
    // (You can use LAPACK for QR decomposition here)

    // Compute B = Q^T * A
    // (You can use LAPACK for SVD here)

    free(Omega);
    free(Y);
}