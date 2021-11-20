def binary_search(arr, low, high, x):
    arr = sorted(arr)
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return "at index: " + str(mid)
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return "not present in list!!"


if __name__ == '__main__':
    import numpy as np
    array = np.random.randint(1, 30, 10)
    print(sorted(array))
    print(binary_search(array, 0, len(array) - 1, 9))