def quicksort_custom(arr):
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Args:
        arr (list): The list of comparable elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    return quicksort_custom(less) + [pivot] + quicksort_custom(greater)


if __name__ == "__main__":
    # Example usage
    sample = [5, 3, 8, 4, 2, 7, 1, 10]
    print("Original list:", sample)
    sorted_list = quicksort_custom(sample)
    print("Sorted list:", sorted_list)
