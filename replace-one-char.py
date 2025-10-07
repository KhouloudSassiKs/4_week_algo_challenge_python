def replace_character(input_string: str, c1: str, c2: str) -> str:
    """
    Replace all occurrences of character `c1` in `input_string` with `c2`.

    Args:
        input_string (str): The original string.
        c1 (str): Character to replace.
        c2 (str): Replacement character.

    Returns:
        str: The processed string with replacements.
    """
    processed_string = ""

    for letter in input_string:
        if letter == c1:
            processed_string += c2
        else:
            processed_string += letter

    return processed_string


# Example usage
print(replace_character("banana", "a", "o"))   # bonono
print(replace_character("hello world", "l", "x"))  # hexxo worxd
