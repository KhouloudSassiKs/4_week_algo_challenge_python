def solution(numbers):
    """Return the given list in reverse order using a traditional for loop."""
    output = []
    for i in range(len(numbers) - 1, -1, -1):
        output.append(numbers[i])
    return output


if __name__ == "__main__":
    # Example usages
    print(solution([1, 2, 3, 4, 5]))   # Output: [5, 4, 3, 2, 1]
    print(solution(['x', 'y', 'z']))   # Output: ['z', 'y', 'x']
    print(solution([]))                # Output: []
