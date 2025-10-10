def shift_list_elements(ls, shift):
    """
    Shift the elements of a list circularly by 'shift' positions.
    
    Positive shift -> move elements to the right.
    Negative shift -> move elements to the left.
    """
    if not ls:
        return []

    # Normalize shift to avoid unnecessary full rotations
    shift %= len(ls)

    output = [0 for _ in range(len(ls))]

    for i in range(len(ls)):
        new_pos = i + shift
        if new_pos < 0:
            new_pos += len(ls)
        elif new_pos >= len(ls):
            new_pos -= len(ls)
        output[new_pos] = ls[i]

    return output


if __name__ == "__main__":
    # Example usages
    print(shift_list_elements([1, 2, 3, 4, 5], 2))    # Output: [4, 5, 1, 2, 3]
    print(shift_list_elements([1, 2, 3, 4, 5], -1))   # Output: [2, 3, 4, 5, 1]
    print(shift_list_elements(['a', 'b', 'c'], 4))    # Output: ['c', 'a', 'b']
    print(shift_list_elements([], 3)) 
