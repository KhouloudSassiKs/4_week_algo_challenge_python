def find_most_common_substring(s: str, length: int) -> str:
    # TODO: implement the function
    if len(s) < length:
        return ""

    best_substring = ""
    best_count = 0
    substring_dict = {}

    for index in range(len(s) - length + 1):
        substring = s[index:index + length]
        substring_dict[substring] = substring_dict.get(substring, 0) + 1
        count = substring_dict[substring]

        if count > best_count:
            best_count = count
            best_substring = substring
        elif count == best_count and substring < best_substring:
            best_substring = substring

    return best_substring


if __name__ == "__main__":
    print(find_most_common_substring("abababab", 2))  # ab
    print(find_most_common_substring("zyxwvutsr", 1)) # r
    print(find_most_common_substring("aaaa", 1))      # a
