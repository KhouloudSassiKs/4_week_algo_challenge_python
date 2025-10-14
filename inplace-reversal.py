def solution(arr: list[int]) -> list[int]:
    """
    Reverses the array in-place without using built-in reverse methods.

    Args:
        arr (list[int]): The list to reverse.

    Returns:
        list[int]: The same list, reversed in-place.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    print("Original:", numbers)
    print("Reversed:", solution(numbers))
