from typing import List

#Implements the Quickselect algorithm to find the kth smallest element in a sorted array
def QuickSelect(arr: List[int | float], k: int):
    # Standard Lomuto partition function
    def partition(arr, low, high):
        pivot = arr[high]
        i = (low - 1)
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    left, right = 0, len(arr) - 1
    while left <= right:
        pivotIndex = partition(arr, left, right)

        if pivotIndex == k - 1:
            return arr[pivotIndex]
        elif pivotIndex > k - 1:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1

    return -1