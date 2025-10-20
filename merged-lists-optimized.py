def merge_n_sorted_lists(arr: list[list[int]]) -> list[int]:
    """Merge multiple sorted lists into a single sorted list."""
    output = []
    for i in range(len(arr)):
        output = merge_lists(output, arr[i])
    return output


def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list."""
    index1 = index2 = 0
    merged = []

    while index1 < len(list1) and index2 < len(list2):
        el1 = list1[index1]
        el2 = list2[index2]

        if el1 < el2:
            merged.append(el1)
            index1 += 1
        elif el1 == el2:
            merged.append(el1)
            merged.append(el2)
            index1 += 1
            index2 += 1
        else:
            merged.append(el2)
            index2 += 1  

    remaining = list1[index1:] if index1 < len(list1) else list2[index2:]
    return merged + remaining


if __name__ == "__main__":
    # Example usage
    sample_input = [[1, 3, 5], [2, 3, 6], [0, 4, 4]]
    print(merge_n_sorted_lists(sample_input))  # Expected: [0, 1, 2, 3, 3, 4, 4, 5, 6]
