def merge_sort(lst):
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Args:
        lst (list): The list of comparable elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): The left sorted sublist.
        right (list): The right sorted sublist.

    Returns:
        list: The merged and sorted list.
    """
    i = j = 0
    merged = []

    # Compare elements from both halves and merge them in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    merged += left[i:] + right[j:]
    return merged


if __name__ == "__main__":
    # Example usage
    sample = [5, 3, 8, 4, 2]
    print("Original list:", sample)
    sorted_list = merge_sort(sample)
    print("Sorted list:", sorted_list)
