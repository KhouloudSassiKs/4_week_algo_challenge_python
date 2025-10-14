def find_row_with_target(matrix: list[list[int]], target: int) -> int | None:
    """
    Returns the row index containing the target value in an ascending order sorted natrix.
    Returns None if the target is not find in the matrix.
    Starts searching from the bottom-left corner for efficiency.
    """
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1
    i = rows
    j = 0

    while i >= 0 and j <= cols:
        if matrix[i][j] == target:
            return i
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1

    return None


if __name__ == "__main__":
    # Example usage
    matrix = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17]
    ]
    
    target = 9
    result = find_row_with_target(matrix, target)
    
    if result is not None:
        print(f"Target {target} is in row {result}.")
    else:
        print(f"Target {target} not found in the matrix.")
