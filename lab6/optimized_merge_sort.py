comparison_count = 0
copy_count = 0

def insertion_sort(arr, left, right):
    global comparison_count
    global copy_count

    for i in range(left + 1, right + 1):
        key = arr[i]
        copy_count += 1
        j = i - 1
        while j >= left and arr[j] > key:
            comparison_count += 1
            arr[j + 1] = arr[j]
            copy_count += 1
            j -= 1
        arr[j + 1] = key
        copy_count += 1

def merge(arr, aux, left, mid, right):
    global comparison_count
    global copy_count

    if mid == right or arr[mid] <= arr[mid + 1]:
        return

    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        comparison_count += 1
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            copy_count += 1
            i += 1
        else:
            aux[k] = arr[j]
            copy_count += 1
            j += 1
        k += 1

    while i <= mid:
        aux[k] = arr[i]
        copy_count += 1
        i += 1
        k += 1

    while j <= right:
        aux[k] = arr[j]
        copy_count += 1
        j += 1
        k += 1

    arr[left:right+1] = aux[left:right+1]
    copy_count += (right - left + 1)

def merge_sort(arr):
    global comparison_count
    global copy_count

    n = len(arr)
    aux = arr.copy()
    CUT_OFF = 10

    curr_size = 1
    while curr_size < n:
        left = 0
        while left < n:
            mid = min(left + curr_size -1, n -1)
            right = min(left + 2 * curr_size -1, n -1)

            if right - left <= CUT_OFF:
                insertion_sort(arr, left, right)
            else:
                merge(arr, aux, left, mid, right)

            left += 2 * curr_size
        curr_size *= 2
