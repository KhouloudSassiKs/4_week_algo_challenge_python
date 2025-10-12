def solution(n):
    """
    Recursively generate a list of integers from n down to 1.
    Example: solution(5) -> [5, 4, 3, 2, 1]
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    return [n] + solution(n - 1)


if __name__ == "__main__":
    # Example usages
    print(solution(1))   # Output: [1]
    print(solution(3))   # Output: [3, 2, 1]
    print(solution(5))   # Output: [5, 4, 3, 2, 1]
    print(solution(0))   # Output: []
    
