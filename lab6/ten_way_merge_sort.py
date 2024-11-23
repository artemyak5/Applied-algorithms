from counters import Counter

def merge(arr, left, mid, right, counter):
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
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

    while i < len(L):
        arr[k] = L[i]
        counter.copy_count += 1
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        counter.copy_count += 1
        j += 1
        k += 1

def merge_sort(arr, counter):
    n = len(arr)
    chunk_size = max(1, n // 10)
    curr_size = chunk_size

    while curr_size < n:
        left = 0
        while left < n:
            mid = min(left + curr_size -1, n -1)
            right = min(left + 2 * curr_size -1, n -1)
            merge(arr, left, mid, right, counter)
            left += 2 * curr_size
        curr_size *= 2
