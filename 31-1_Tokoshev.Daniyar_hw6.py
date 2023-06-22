def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(element, arr):
    first = 0
    last = len(arr) - 1
    resultOK = False
    result = None
    while first < last:
        mid = (first + last) // 2

        if arr[mid] == element:
            first = last = mid
            resultOK = True
            result = mid
            break
        elif arr[mid] < element:
            first = mid + 1
        else:
            last = mid - 1

    if resultOK:
        print(f"Элемент найден на позиции {result}.")
    else:
        print("Элемент не найден.")

    print("Конец")


bubble_sort([1, 2, 2, 2, 3, 1, 4, 3])
binary_search(20, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
