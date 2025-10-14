from typing import List

def anti_rotate_array(nums: List[int], k: int) -> List[int]:
    """
    Rotates the array `nums` anti-clockwise (to the left) by `k` steps.
    The rotation is done inplace.
    K can be bigger than len(nums)
    Args:
        nums (List[int]): The list of integers to rotate.
        k (int): The number of rotation steps.

    Returns:
        List[int]: The rotated list.
    """
    if not nums:
        return nums

    rotation = k % len(nums)  # Handle cases where k > len(nums)
    
    for _ in range(rotation):
        first = nums[0]
        for j in range(len(nums) - 1):
            nums[j] = nums[j + 1]
        nums[-1] = first

    return nums


if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    print("Original array:", numbers)
    rotated = anti_rotate_array(numbers, k)
    print(f"Array after anti-clockwise rotation by {k} steps:", rotated)
