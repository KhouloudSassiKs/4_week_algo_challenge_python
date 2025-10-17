def solution(strs):
    """Return the longest common suffix among a list of strings."""
    
    if not strs:
        return ""
    
    # Reverse each string to find common prefix (which becomes suffix when reversed back)
    rev_strs = [word[::-1] for word in strs]
    common_suffix = rev_strs[0]

    for word in rev_strs:
        new_suffix = ""
        comp_length = min(len(word), len(common_suffix))
        
        for index in range(comp_length):
            if word[index] == common_suffix[index]:
                new_suffix += common_suffix[index]
            else:
                break

        if not new_suffix:
            return ""
        
        common_suffix = new_suffix

    return common_suffix[::-1]


if __name__ == "__main__":
    # Example usage
    examples = [
        ["running", "jogging", "walking"],
        ["fishing", "wishing", "dishing"],
        ["cat", "bat", "rat"],
        ["hello", "yellow", "mellow"],
        ["dog", "cat", "fish"]
    ]

    for words in examples:
        result = solution(words)
        print(f"Strings: {words}")
        print(f"Longest common suffix: '{result}'")
        print("-" * 40)
