from typing import List, Optional

def second_max(nums: List[int]) -> Optional[int]:
    """
    Find the second largest unique integer in the list.

    Args:
        nums (List[int]): List of integers.

    Returns:
        Optional[int]: The second largest integer, or None if it doesn't exist.
    """
    if len(nums) < 2:
        return None

    largest = nums[0]
    second_largest = None

    for number in nums:
        if number > largest:
            second_largest = largest
            largest = number
        elif number < largest:
            if second_largest is None or number > second_largest:
                second_largest = number

    return second_largest


# Example usage
if __name__ == "__main__":
    example_list = [5, 1, 4, 2, 5]
    print(f"{example_list} -> {second_max(example_list)}")  # Output: 4
