# Function to add two matrices
def add_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

# Function to subtract two matrices
def subtract_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

# Function to multiply two matrices
def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result

# Function to transpose a matrix
def transpose_matrix(A):
    result = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        result.append(row)
    return result

# Example matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Matrix Operations
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

# Addition
print("\nAddition of A and B:")
addition_result = add_matrices(A, B)
for row in addition_result:
    print(row)

# Subtraction
print("\nSubtraction of A and B:")
subtraction_result = subtract_matrices(A, B)
for row in subtraction_result:
    print(row)

# Multiplication
print("\nMultiplication of A and B:")
multiplication_result = multiply_matrices(A, B)
for row in multiplication_result:
    print(row)

# Transpose of Matrix A
print("\nTranspose of Matrix A:")
transpose_result = transpose_matrix(A)
for row in transpose_result:
    print(row)
