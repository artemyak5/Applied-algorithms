from counters import Counter

def merge(arr, left, mid, right, counter):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        counter.comparison_count += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            counter.copy_count += 1
            i += 1
        else:
            arr[k] = R[j]
            counter.copy_count += 1
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        counter.copy_count += 1
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        counter.copy_count += 1
        j += 1
        k += 1

def merge_sort(arr, counter):
    n = len(arr)
    curr_size = 1

    while curr_size < n:
        left = 0
        while left < n-1:
            mid = min((left + curr_size - 1), n - 1)
            right = min((left + 2 * curr_size -1), n - 1)
            merge(arr, left, mid, right, counter)
            left += 2 * curr_size
        curr_size *= 2
