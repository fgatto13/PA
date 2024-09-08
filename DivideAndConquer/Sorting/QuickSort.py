import random

def Swap(A, i, j):
    A[i], A[j] = A[j], A[i]
# this selects the pivot always in the middle (best if we know that the array is nearly sorted)

def Partition(A, low, high) -> int:
    mid = (low + high) // 2
    Swap(A, low, mid)  # Move the middle element to the low position
    pivot = A[low]
    i = low
    j = high
    while i < j:
        while A[i] <= pivot and i < high:
            i += 1
        while A[j] > pivot and j > low:
            j -= 1
        if i < j:
            Swap(A, i, j)
    Swap(A, low, j)
    return j

# this selects the pivot in a random position in A, making it way harder to get a worst case scenario

def Partition_random(A, low, high) -> int:
    rand_pivot = random.randint(low, high)
    Swap(A, low, rand_pivot)  # Move the random element to the low position
    pivot = A[low]
    i = low
    j = high
    while i < j:
        while A[i] <= pivot and i < high:
            i += 1
        while A[j] > pivot and j > low:
            j -= 1
        if i < j:
            Swap(A, i, j)
    Swap(A, low, j)
    return j

def QuickSort(A, low, high):
    if low < high:
        j = Partition_random(A, low, high)
        QuickSort(A, low, j - 1)  # Recursively sort the left part
        QuickSort(A, j + 1, high) # Recursively sort the right part
