def merge_n_sorted_lists(arr: list[list[int]]) -> list[int]:
    """Merge multiple sorted lists into a single sorted list."""
    # TODO: implement the function to merge sorted lists
    output = []
    element_dict = {}

    # Count occurrences of each element across all lists
    for ar in arr:
        for element in ar:
            element_dict[element] = element_dict.get(element, 0) + 1

    # Append elements to output in sorted order
    while element_dict:
        min_element = min(element_dict)
        output += [min_element] * element_dict[min_element]
        del element_dict[min_element]

    return output


if __name__ == "__main__":
    # Example usage
    sample_input = [[1, 3, 5], [2, 3, 6], [0, 4, 4]]
    print(merge_n_sorted_lists(sample_input))  # Expected: [0, 1, 2, 3, 3, 4, 4, 5, 6]
