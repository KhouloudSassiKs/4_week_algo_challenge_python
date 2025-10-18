def largest_common_prefix(words):
    """
    Finds the largest common prefix among a list of words.
    Returns an empty string if:
    - there is no common prefix.
    - the input array is empty.
    - the input array has one word.
    """
    if not words or len(words) < 2:
        return ""

    common_prefix = words[0]

    for word in words[1:]:
        # Compare characters up to the length of the current common prefix
        iter_len = min(len(common_prefix), len(word))
        prefix = ""
        for i in range(iter_len):
            if common_prefix[i] == word[i]:
                prefix += common_prefix[i]
            else:
                break
        if not prefix:
            return ""
        common_prefix = prefix

    return common_prefix
  if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        ["throne", "throne"],
        ["prefix"]
    ]

    for words in test_cases:
        print(f"{words} -> '{largest_common_prefix(words)}'")
