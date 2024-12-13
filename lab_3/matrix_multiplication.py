def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Liczba kolumn w macierzy A musi być równa liczbie wierszy w macierzy B.")

    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


matrix_a = [[1, 2, 3],[4, 5, 6]]

matrix_b = [[7, 8],[9, 10],[11, 12]]

print("Macierz wynikowa:", multiply_matrices(matrix_a, matrix_b))