comparison_count = 0
copy_count = 0

def merge_sort(arr):
    global comparison_count
    global copy_count

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    global comparison_count
    global copy_count

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        comparison_count += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            copy_count += 1
            i += 1
        else:
            merged.append(right[j])
            copy_count += 1
            j += 1

    while i < len(left):
        merged.append(left[i])
        copy_count += 1
        i += 1

    while j < len(right):
        merged.append(right[j])
        copy_count += 1
        j += 1

    return merged
