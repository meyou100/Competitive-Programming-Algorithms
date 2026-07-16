from typing import List

#Implements the Quickselect algorithm to find the kth smallest element in a nonsorted array
def QuickSelect(arr: List[int | float], k: int) -> int | float:
    # Standard Lomuto partition function
    def partition(arr: List[int | float], low: int, high: int) -> int:
        pivot = arr[high] #pick the last element as the pivot
        i = (low - 1)
        for j in range(low, high): #puts all numbers <= pivot in the first part of the array
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1 #returns pivot's place in the array

    left, right = 0, len(arr) - 1
    while left <= right:
        pivotIndex = partition(arr, left, right)

        if pivotIndex == k - 1: #if the index of the pivot is k then return the element
            return arr[pivotIndex]
        elif pivotIndex > k - 1: #if the index is > k then the kth smallest element is in the first part of the array
            right = pivotIndex - 1
        else: #if the index < k then the kth smallest element is in the latter part of the array
            left = pivotIndex + 1

