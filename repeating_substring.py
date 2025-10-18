def repeat_substring(s: str) -> str:
    """
    Returns the longest repeating substring in an input string `s`.
    If no repeating substring is found, return an empty string.
    """
    initial_len = len(s)
    
    for div_len in range(initial_len - 1, 0, -1):
        if initial_len % div_len == 0:
            substring = s[:div_len]
            if s == substring * (initial_len // div_len):
                return substring
                
    return ""


if __name__ == "__main__":
    tests = ["abababab", "abcabcabc", "aaaaaa", "abcd", "abcabcab"]

    for t in tests:
        print(f"{t} → '{repeat_substring(t)}'")
