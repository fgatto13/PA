from QuickSort import Partition_random

def QuickSelect(A, low, high, k):
    if low == high:
        return A[low]  # Only one element, base case

    pivot_index = Partition_random(A, low, high)  # Partition and get pivot's position
    rank = pivot_index - low + 1  # Rank of the pivot in the array

    if rank == k:  # Found the k-th element
        return A[pivot_index]
    elif k < rank:  # The k-th element is in the left partition
        return QuickSelect(A, low, pivot_index - 1, k)
    else:  # The k-th element is in the right partition
        return QuickSelect(A, pivot_index + 1, high, k - rank)

# For finding k-th largest
def QuickSelect_kth_max(A, low, high, k):
    n = len(A)
    return QuickSelect(A, low, high, n - k + 1)

# Example usage
A = [2, 1, 5, 4, 6, 18, 10, 13, 12, 24, 3]
k_min = 3  # Finding the 3rd smallest
k_max = 2  # Finding the 2nd largest
print("3rd smallest:", QuickSelect(A, 0, len(A) - 1, k_min))
print("2nd largest:", QuickSelect_kth_max(A, 0, len(A) - 1, k_max))