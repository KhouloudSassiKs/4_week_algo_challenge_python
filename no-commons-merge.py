def remove_common_elements(list1, list2):
    index1 = index2 = 0
    list3 = []

    while index1 < len(list1) and index2 < len(list2):
        element1 = list1[index1]
        element2 = list2[index2]

        if element1 < element2:
            if element1 not in list2:
                list3.append(element1)
            index1 += 1
        elif element2 < element1:
            if element2 not in list1:
                list3.append(element2)
            index2 += 1
        else:
            # Skip common elements
            index1 += 1
            index2 += 1

    # Add remaining elements from list1
    for number in list1[index1:]:
        if number not in list2:
            list3.append(number)

    # Add remaining elements from list2
    for number in list2[index2:]:
        if number not in list1:
            list3.append(number)

    return list3


if __name__ == "__main__":
    print(remove_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [1, 2, 5, 6]
    print(remove_common_elements([1, 2], [1, 2]))              # []
    print(remove_common_elements([1, 3, 5], [2, 4, 6]))        # [1, 3, 5, 2, 4, 6]
    print(remove_common_elements([], [1, 2]))   
