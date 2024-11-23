from counters import Counter

def merge_sort(arr, counter):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counter)
    right = merge_sort(arr[mid:], counter)

    return merge(left, right, counter)

def merge(left, right, counter):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        counter.comparison_count += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            counter.copy_count += 1
            i += 1
        else:
            merged.append(right[j])
            counter.copy_count += 1
            j += 1

    while i < len(left):
        merged.append(left[i])
        counter.copy_count += 1
        i += 1

    while j < len(right):
        merged.append(right[j])
        counter.copy_count += 1
        j += 1

    return merged
