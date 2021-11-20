
def binary_earch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            return mid
    else:
        return -1


def binary_search(list, x):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < x:
            low = mid + 1
        elif list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


#
# test
list = [1, 3, 5, 7, 9]
result = binary_earch(list, 9)
print(result)
