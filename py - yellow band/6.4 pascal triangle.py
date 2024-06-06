def print_pascals_triangle(n):
    """
    Prints the first n rows of Pascal's triangle.

    Parameters:
    n (int): The number of rows of Pascal's triangle to print.
    """
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    for row in triangle:
        print(' '.join(map(str, row)))


# Example usage:
rows = 5
print(f"First {rows} rows of Pascal's Triangle:")
print_pascals_triangle(rows)
