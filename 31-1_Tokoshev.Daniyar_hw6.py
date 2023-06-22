def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def binary_search(element, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            print(mid)
            break
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1


bubble_sort([1, 2, 2, 2, 3, 1, 4, 3])
binary_search(20, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
