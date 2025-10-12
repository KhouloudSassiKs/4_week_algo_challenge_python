def reverse_string(s):
    """
    Recursively reverse the input string.
    
    Example:
        reverse_string("hello") -> "olleh"
    """
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])


if __name__ == "__main__":
    # Example usages
    print(reverse_string("hello"))   # Output: "olleh"
    print(reverse_string("Python"))  # Output: "nohtyP"
    print(reverse_string(""))        # Output: ""
