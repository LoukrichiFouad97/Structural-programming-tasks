def matrix_addition(matrix1, matrix2):
    result = []

    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    # Perform matrix addition
    for i in range(len(matrix1)):
        row_result = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        result.append(row_result)

    return result

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = [float(input(f"Enter element for row {i + 1}, column {j + 1}: ")) for j in range(cols)]
        matrix.append(row)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    print("Enter elements for the first matrix:")
    matrix1 = input_matrix()

    print("\nEnter elements for the second matrix:")
    matrix2 = input_matrix()

    try:
        result = matrix_addition(matrix1, matrix2)
        print("\nMatrix1:")
        display_matrix(matrix1)
        print("\nMatrix2:")
        display_matrix(matrix2)
        print("\nMatrix Addition (Matrix1 + Matrix2):")
        display_matrix(result)

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
