def solution(input_string):
    """
    Transform each letter in the string:
    - Lowercase letters → Uppercase
    - Uppercase letters → Lowercase
    - Non-alphabetic characters remain unchanged
    """
    transformed_string = ""

    for letter in input_string:
        letter_code = ord(letter)

        if ord('a') <= letter_code <= ord('z'):
            transformed_string += chr(letter_code - 32)  # to uppercase
        elif ord('A') <= letter_code <= ord('Z'):
            transformed_string += chr(letter_code + 32)  # to lowercase
        else:
            transformed_string += letter

    return transformed_string


# Example usage
print(solution("Hello World!"))  # hELLO wORLD!
print(solution("Python3"))       # pYTHON3
