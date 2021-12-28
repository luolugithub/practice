def quick_sort(lists):
    """
    simple full code for quick sort
    """
    if len(lists) <= 1:
        return lists
    pivot = lists[0]

    left_list = []
    right_list = []
    for x in lists[1:]:
        if x < pivot:
            left_list.append(x)
        else:
            right_list.append(x)
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


# *********************** method 2 **************************************

def partion(arr, left, right):
    if left >= right:
        return
    pivot_index = left
    while left < right:
        while left < right and arr[left] <= arr[pivot_index]:
            left += 1
        while arr[right] > arr[pivot_index]:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    return right


def quick_sort(arr, left, right):
    if left < right:
        p = partion(arr, left, right)
        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)
    return arr


if __name__ == '__main__':
    import numpy as np

    array = np.random.randint(1, 30, 10)
    print(array)
    print(quick_sort(array, 0, len(array) - 1))
