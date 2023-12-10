def binary_search(lst: list, item: int) -> int:
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guss = lst[mid]
        if guss == item:
            return mid
        if guss > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


lst = [1, 4, 5, 7, 9, 12, 45, 56, 78, 87, 98, 112]
print(binary_search(lst, 98))