def solution(s):
    """
    Swap every two adjacent characters in the string.
    If the string has an odd length, the last character stays in place.

    Args:
        s (str): Input string.

    Returns:
        str: Processed string with swapped pairs.
    """
    length = len(s)
    if length == 1:
        return s

    processed_string = ""

    # If odd length, save the last character separately
    added_char = ''
    final_index = length
    if length % 2 == 1:
        final_index -= 1
        added_char = s[-1]

    # Swap pairs
    for index in range(0, final_index, 2):
        processed_string += s[index + 1] + s[index]

    # Add leftover char if odd length
    processed_string += added_char

    return processed_string


# Example usage
print(solution("abcd"))   # "badc"
print(solution("abcde"))  # "badce"
print(solution("a"))      # "a"
