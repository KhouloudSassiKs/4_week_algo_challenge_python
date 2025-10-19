def merge_sorted_lists_descending_unique(l1, l2):
    l3 = []
    index1 = index2 = 0

    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] < l2[index2]:
            if l1[index1] not in l3:
                l3.append(l1[index1])
            index1 += 1
        elif l1[index1] == l2[index2]:
            if l1[index1] not in l3:
                l3.append(l1[index1])
            index1 += 1
            index2 += 1
        else:
            if l2[index2] not in l3:
                l3.append(l2[index2])
            index2 += 1

    # Add remaining elements
    remaining = l1[index1:] if index1 < len(l1) else l2[index2:]
    for number in remaining:
        if number not in l3:
            l3.append(number)

    # Return in descending order
    return l3[::-1]


if __name__ == "__main__":
    print(merge_sorted_lists_descending_unique([1, 3, 5], [2, 3, 4]))  # [5, 4, 3, 2, 1]
    print(merge_sorted_lists_descending_unique([1, 2, 2], [2, 3]))     # [3, 2, 1]
    print(merge_sorted_lists_descending_unique([], [1, 2, 3]))          # [3, 2, 1]
    print(merge_sorted_lists_descending_unique([5, 6], []))      
