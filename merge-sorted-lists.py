def solution(l1, l2):
    # TODO: implement the function to merge two lists and return the merged list
    index1 = index2 = 0
    l3 = []

    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] < l2[index2]:
            l3.append(l1[index1])
            index1 += 1
        elif l1[index1] == l2[index2]:
            l3.append(l1[index1])
            l3.append(l2[index2])
            index1 += 1
            index2 += 1
        else:
            l3.append(l2[index2])
            index2 += 1

    # Append the remaining elements from whichever list is not yet finished
    remaining = l1[index1:] if index1 < len(l1) else l2[index2:]

    return l3 + remaining


if __name__ == "__main__":
    print(solution([1, 3, 5], [2, 4, 6]))       # [1, 2, 3, 4, 5, 6]
    print(solution([1, 2, 3], [3, 4, 5]))       # [1, 2, 3, 3, 4, 5]
    print(solution([], [1, 2, 3]))              # [1, 2, 3]
    print(solution([1, 2, 3], []))              # [1, 2, 3]
