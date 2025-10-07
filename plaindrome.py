def solution(input_string):
    """
    Check if the input string is a palindrome, ignoring non-alphanumeric characters
    and treating uppercase and lowercase letters as equal.
    """
    if not input_string:
        return True

    processed_string = ""
    for letter in input_string:
        code = ord(letter)
        # Keep only alphanumeric characters
        if 48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122:
            # Convert uppercase to lowercase
            if 65 <= code <= 90:
                code += 32
            processed_string += chr(code)

    # Two-pointer palindrome check
    left = 0
    right = len(processed_string) - 1
    while left <= right:
        if processed_string[left] != processed_string[right]:
            return False
        left += 1
        right -= 1

    return True


# Example usage
if __name__ == "__main__":
    examples = ["A man, a plan, a canal: Panama", "hello", ""]
    for s in examples:
        print(f"'{s}' -> {solution(s)}")
