def solution(listA, listB):
    """
    Check if listB appears as a contiguous sublist within listA.
    Returns True if found, otherwise False.
    """
    len_A = len(listA)
    len_B = len(listB)

    # Edge case: empty listB is always considered contained
    if len_B == 0:
        return True

    index_A = 0
    while index_A <= len_A - len_B:
        if listA[index_A:index_A + len_B] == listB:
            return True
        index_A += 1

    return False


if __name__ == "__main__":
    # Example usages
    print(solution([1, 2, 3, 4, 5], [2, 3]))     # True
    print(solution([1, 2, 3, 4, 5], [3, 5]))     # False
    print(solution(['a', 'b', 'c', 'd'], ['b', 'c']))  # True
    print(solution([1, 2, 3], []))               # True (empty listB)
    print(solution([], [1]))  
