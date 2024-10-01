import random

def Partition(A, low, high) -> int:
    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]  # Move the middle element to the low position
    pivot = A[low]
    i = low
    j = high
    while i < j:
        while A[i] <= pivot and i < high:
            i += 1
        while A[j] > pivot and j > low:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[low], A[j] = A[j], A[low]
    return j

# this selects the pivot in a random position in A, making it way harder to get a worst case scenario

def Partition_random(A, low, high) -> int:
    rand_pivot = random.randint(low, high)
    A[low], A[rand_pivot] = A[rand_pivot], A[low]  # Move the random element to the low position
    pivot = A[low]
    i = low
    j = high
    while i < j:
        while A[i] <= pivot and i < high:
            i += 1
        while A[j] > pivot and j > low:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[low], A[j] = A[j], A[low]
    return j

def QuickSort(A, low, high):
    if low < high:
        j = Partition_random(A, low, high)
        QuickSort(A, low, j - 1)  # Recursively sort the left part
        QuickSort(A, j + 1, high) # Recursively sort the right part
