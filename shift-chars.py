def solution(s: str) -> str:
    """
    Shift each alphabetical character by 1.
    - 'a'..'y' → next letter
    - 'z' → 'a'
    - 'A'..'Y' → next uppercase letter
    - 'Z' → 'A'
    Non-alphabet characters remain unchanged.
    """
    output_shifted_string = ""

    for letter in s:
        code_ascii_letter = ord(letter)

        if letter == 'z':
            output_shifted_string += 'a'
        elif letter == 'Z':
            output_shifted_string += 'A'
        elif (ord('a') <= code_ascii_letter < ord('z')) or (ord('A') <= code_ascii_letter < ord('Z')):
            output_shifted_string += chr(code_ascii_letter + 1)
        else:
            output_shifted_string += letter

    return output_shifted_string


# Example usage
print(solution("abc xyz"))   # bcd yza
print(solution("XYZ"))       # YZA
print(solution("Hello!"))    # Ifmmp!
