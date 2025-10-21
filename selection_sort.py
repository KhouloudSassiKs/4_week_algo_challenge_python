def selection_sort(arr: list[int]) -> list[int]:
    """Sort a list of numbers in ascending order using the selection sort algorithm."""
    # TODO: Implement selection sort algorithm
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    # Example usage
    sample = [64, 25, 12, 22, 11]
    print(selection_sort(sample))  # Expected output: [11, 12, 22, 25, 64]
