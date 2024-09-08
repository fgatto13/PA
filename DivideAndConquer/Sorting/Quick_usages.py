from QuickSort import QuickSort
from QuickSelect import QuickSelect, QuickSelect_kth_max

# Example usage
A = [2, 1, 5, 4, 6, 18, 10, 13, 12, 24, 3]
print("Before sorting:", A)
QuickSort(A, 0, len(A) - 1)
print("After sorting:", A)