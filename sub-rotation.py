from typing import List

def solution(numbers: List[int], k: int) -> List[int]:
    """
    Reverses elements of the list `numbers` in sub groups of size `k`.
    k less than len of numbers.
    Args:
        numbers (List[int]): The list of integers to process.
        k (int): Size of each group to reverse.

    Returns:
        List[int]: A new list with each group of size `k` reversed.
    """
    output = []
    counter = 1  # Tracks position in the list

    for number in numbers:
        # Handle completed groups of size k
        if counter % k == 0:
            for j in range(counter - 1, counter - k - 1, -1):
                output.append(numbers[j])
        # Handle the final group if its size is less than k
        elif counter == len(numbers):
            remaining = counter % k
            for j in range(counter - 1, counter - remaining - 1, -1):
                output.append(numbers[j])
        counter += 1

    return output


if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    result = solution(numbers, k)
    print("Original list:", numbers)
    print(f"List after reversing in groups of {k}:", result)
