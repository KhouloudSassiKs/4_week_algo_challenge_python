def efficient_LCP(strs):
    """
    Finds the largest common prefix among a list of strings using sorting.
    Efficient because it only compares the first and last words after sorting.

    Args:
        strs (list[str]): List of strings to find the common prefix.

    Returns:
        str: The longest common prefix, or empty string if none exists.

    Example:
        efficient_LCP(["flower","flow","flight"]) -> "fl"
        efficient_LCP(["dog","racecar","car"]) -> ""
    """
    if not strs or len(strs) < 2:
        return ""

    # Sort strings alphabetically
    sorted_strs = sorted(strs)
    first, last = sorted_strs[0], sorted_strs[-1]
    prefix = ""
    iter_len = min(len(first), len(last))

    # Compare characters of first and last word only
    for i in range(iter_len):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            break

    return prefix
  
  if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        ["throne", "throne"],
        ["prefix"]
    ]

    for words in test_cases:
        print(f"{words} -> '{efficient_LCP(words)}'")
