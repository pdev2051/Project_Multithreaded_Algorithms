import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Multiply one row of A with all columns of B
def compute_row(A, B, row_index):
    result_row = []
    for j in range(B.shape[1]):
        value = sum(A[row_index][k] * B[k][j] for k in range(B.shape[0]))
        result_row.append(value)
    return row_index, result_row

def threaded_matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Number of columns in A must equal number of rows in B")

    result = np.zeros((A.shape[0], B.shape[1]), dtype=int)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(compute_row, A, B, i) for i in range(A.shape[0])]
        for future in futures:
            row_index, row_values = future.result()
            result[row_index] = row_values

    return result

# Example usage
def main():
    A = np.array([[1, 2], [3, 4], [5, 6]])
    B = np.array([[7, 8, 9], [10, 11, 12]])

    result = threaded_matrix_multiply(A, B)
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("Result of A x B:\n", result)

if __name__ == "__main__":
    main()
