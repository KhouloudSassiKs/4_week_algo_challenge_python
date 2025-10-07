def solution(s: str) -> list[int]:
    """
    Return a list of 0 based positions of the vowels in the input string.

    Args:
        s: The input string.

    Returns:
        list[int]: A list of indexes where vowels occur in the string.

    Example:
       solution("Hello World")
        >>>> [1, 4, 7]
    """
    vowels = "aeiou"
    vowel_positions = []

    for index, letter in enumerate(s):
        if letter.lower() in vowels:
            vowel_positions.append(index)

    return vowel_positions


# Example usage
print(solution("Hello World"))   # [1, 4, 7]
print(solution("Python"))        # [4]
print(solution("Sky"))           # []
