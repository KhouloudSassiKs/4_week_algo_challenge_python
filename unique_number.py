def count_unique_elements(lst):
    """Return the number of unique (non-repeated) elements in the list."""
    visited = []
    unique_count = 0

    for i in range(len(lst)):
        current_number = lst[i]

        if current_number in visited:
            continue
        visited.append(current_number)

        # Check if current_number appears again later
        found = False
        for j in range(i + 1, len(lst)):
            if lst[j] == current_number:
                found = True
                break

        if not found:
            unique_count += 1

    return unique_count


if __name__ == "__main__":
    print(count_unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Output: 3 (1, 3, 5)
    print(count_unique_elements([10, 10, 20, 30, 30]))   # Output: 1 (20)
    print(count_unique_elements([7, 8, 9]))              # Output: 3 (all unique)
    print(count_unique_elements([]))                     # Output: 0
