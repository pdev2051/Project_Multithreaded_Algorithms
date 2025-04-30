from concurrent.futures import ThreadPoolExecutor
import random

# Merge two sorted lists
def merge(left, right):
    merged = []
    i = j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Recursive multithreaded merge sort
def parallel_merge_sort(arr, executor, depth=0):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # If depth is too deep, fall back to sequential to avoid thread overload
    if depth > 3:
        left = parallel_merge_sort(arr[:mid], executor, depth + 1)
        right = parallel_merge_sort(arr[mid:], executor, depth + 1)
    else:
        # Spawn new threads for both halves
        left_future = executor.submit(parallel_merge_sort, arr[:mid], executor, depth + 1)
        right = parallel_merge_sort(arr[mid:], executor, depth + 1)
        left = left_future.result()

    return merge(left, right)

# Driver function
def main():
    arr = [random.randint(0, 1000) for _ in range(20)]
    print("Original array:", arr)

    with ThreadPoolExecutor() as executor:
        sorted_arr = parallel_merge_sort(arr, executor)

    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
