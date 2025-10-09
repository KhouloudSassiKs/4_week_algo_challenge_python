def solution(lst, val):
    """Return the index of val in lst, or -1 if not found."""
    for i, item in enumerate(lst):
        if item == val:
            return i
    return -1


if __name__ == "__main__":
    # Example usages
    numbers = [10, 20, 30, 40, 50]

    print(solution(numbers, 30))   # Output: 2 (found at index 2)
    print(solution(numbers, 10))   # Output: 0 (found at index 0)
    print(solution(numbers, 50))   # Output: 4 (found at index 4)
    print(solution(numbers, 99))   # Output: -1 (not found)
