def rearrange_array(nums):
    """Rearrange the array by splitting it into four quarters and merging as Q2 + Q3 + Q1 + Q4."""
    
    initial_length = len(nums) // 4
    q1 = q2 = q3 = initial_length
    rest = len(nums) % 4

    # Distribute the remaining elements
    if rest == 1:
        q2 += 1
    elif rest == 2:
        q2 += 1
        q3 += 1
    elif rest == 3:
        q2 += 2
        q3 += 1

    # Compute slice indices
    index1 = q1
    index2 = q1 + q2
    index3 = q1 + q2 + q3

    # Split into quarters
    quarter_one = nums[:index1]
    quarter_two = nums[index1:index2]
    quarter_three = nums[index2:index3]
    quarter_four = nums[index3:]

    # Merge in desired order
    merged = quarter_two + quarter_three + quarter_one + quarter_four

    # Update the original list in place
    for i in range(len(nums)):
        nums[i] = merged[i]


if __name__ == "__main__":
    # Example usage and quick test
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original:", sample)
    rearrange_array(sample)
    print("Rearranged:", sample)
