def solution(string1, string2):
    """Return a string made from characters in string1 that also appear in string2, 
    using each character from string2 at most once."""
    
    output = ""
    dict2 = {}

    # Build frequency dictionary for string2
    for char in string2:
        dict2[char] = dict2.get(char, 0) + 1

    # Construct output based on available characters
    for char in string1:
        if char in dict2 and dict2[char] > 0:
            output += char
            dict2[char] -= 1

    return output


if __name__ == "__main__":
    # Example usage
    s1 = "aabbccddeeff"
    s2 = "abcde"
    result = solution(s1, s2)
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    print(f"Result  : {result}")
