# Bubble sort O(n ^ 2) /  O(n)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    return arr


# %%

# Selection sort O(n ^ 2) / O(n ^ 2)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# %%

# Insertion sort O(n ^ 2) /  O(n)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
            j -= 1
        arr[j + 1] = arr[i]
    return arr


# %%

# Merge sort O(n * log n) / O(n * log n)


def merge(left, right):
    output = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])
    return output


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# %%


# Quicksort O(n * log n) / O(n * log n)
def quicksort(arr):
    if len(arr) <= 3:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)


# %%

# Counting sort O(n + k) / O(k)


def counting_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    sort_range = max_val - min_val + 1
    count_arr = [0] * sort_range
    output = [0] * len(arr)

    for x in arr:
        count_arr[x - min_val] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    return output


# %%


arr = [1, 98, 4, 13, 3, 7, -6, 7]
print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))
print(merge_sort(arr))
print(quicksort(arr))
print(counting_sort(arr))
# %%
