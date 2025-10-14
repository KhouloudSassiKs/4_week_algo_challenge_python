def shuffle_array(nums, k):
    """
    Moves every k-th element of the list `nums` to the end of the list,
    preserving the order of all other elements.
    k always less than the length of the array nums.
    Args:
        nums (list): List of numbers to shuffle.
        k (int): Interval at which elements are moved to the end.

    Returns:
        list: A new list where every k-th element has been moved to the end.
    """
    # Validate input
    if not nums or k <= 0:
        return nums

    counter = 1
    output = []
    moved = []

    # Separate elements into two lists: regular and moved
    for number in nums:
        if counter % k == 0:
            moved.append(number)
        else:
            output.append(number)
        counter += 1

    # Combine both lists: first normal elements, then moved ones
    return output + moved


if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    result = shuffle_array(nums, k)
    print(f"Original list: {nums}")
    print(f"List after moving every {k}-th element: {result}")
