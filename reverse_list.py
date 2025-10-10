def solution(numbers):
    """Return the given list in reverse order."""
    return numbers[::-1]


if __name__ == "__main__":
    # Example usages
    print(solution([1, 2, 3, 4, 5]))   # Output: [5, 4, 3, 2, 1]
    print(solution(['a', 'b', 'c']))   # Output: ['c', 'b', 'a']
    print(solution([]))                # Output: []
