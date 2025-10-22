def insertion_sort(arr):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Args:
        arr (list): The list of comparable elements to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    # Example usage
    sample = [5, 3, 4, 1, 2]
    print("Original array:", sample)
    sorted_array = insertion_sort(sample)
    print("Sorted array:", sorted_array)
