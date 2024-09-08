from QuickSelect import QuickSelect
from QuickSort import Partition_random

# given an array A of unsorted element, create a new array B with the sorted elements
# note: it is not possible to directly confront the elements in A, but it is possible to iteratively call QuickSelect

def Algo(A, n) -> list:
    # create an empty list
    B = []
    # iterate from 0 to n-1
    for i in range(n):
        # what we're doing here is calling QuickSelect for each iteration
        # the point here is to increment the value of k, being the k-th element to look for
        # by doing that, quicksort will look for the i+1th smallest element in A, and returning it
        # so then we insert the element inside the array B
        B.append(QuickSelect(A, 0, n-1, i+1))
    # once the cycle is done, return B
    return B

# time complexity: O(n^2), since for each iteration it has to call QuickSelect (this has a worst time of n^2 based on the pivot chosen)

# given an array A of unsorted elements, and we want to know the 10th biggest element without sorting the array
# solution: we can tweak the algorithm for QuickSelect so that it finds the 10th biggest element in A without sorting it.
# to do it, we basically convert the problem into a k-th smallest by doing k = n - 9, and then we proceede just like a normal QuickSelect

def tenth_largest(A, low, high, n):
    # Find the element of rank 10, which is (n-9) in 0-indexed terms
    k = n - 9
    
    if k <= 0:  # if n < 10, there's no 10th largest element
        return -1

    if low == high:
        return A[low]

    pivot_index = Partition(A, low, high)
    rank = pivot_index - low + 1  # position of pivot in the subarray

    if rank == k:
        return A[pivot_index]
    elif rank > k:
        return tenth_largest(A, low, pivot_index - 1, n)  # Search in left subarray
    else:
        return tenth_largest(A, pivot_index + 1, high, n)  # Search in right subarray
    
# let's now tweak the partitioning function, so that it always starts from the A[high] element
def Partition(A, low, high):
    pivot = A[high]  # choose last element as pivot
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]  # Swap
    A[i + 1], A[high] = A[high], A[i + 1]  # Place pivot in correct position
    return i + 1

# Supponiamo di avere un array di numeri A ordinato in nodo non decrescente e che ciascun elemento appaia al piu` 8 volte in A. 
# Scrivere un algoritmo di divide et impera, quanto piu` efficiente e` possibile, 
# che restituisce una lista contenente tutti gli indici delle celle in cui compare un dato elemento x nell'array A.
# Dire qual e` il tempo di esecuzione del vostro algoritmo nel caso pessimo (non occorre giustificare l'analisi).

# to solve this problem, the best approach would be to use the binary search algorithm to find the position of a given element x
# and then look at both the left and the right side of the position of the element x.
def binary_search_index(A, left, right, x) -> int:
    if left > right:
        return -1
    mid = (left + right) // 2
    if x == A[mid]:
        return mid
    elif A[mid] > x:
        return binary_search_index(A, left, mid-1, x)
    else:
        return binary_search_index(A, mid+1, right, x)
    
# now let's write our solution
def find_instances(A, n, x) -> list:
    pos = binary_search_index(A, 0, n-1, x)
    if pos == -1:
        return []
    
    L = []
    
    # Find all occurrences of x to the right of the found position
    i = pos
    while i < n and A[i] == x:
        L.append(i)
        i += 1

    # Find all occurrences of x to the left of the found position
    i = pos - 1
    while i >= 0 and A[i] == x:
        L.append(i)
        i -= 1
    
    return L
# knowing that the binary search algorithm, even with this tweak, has a time complexity of O(log n)
# the sum of both the while loop cannot be greater than 8 (constrain of the problem)
# therefore, the total amount of iteration of while is fixed to, at most 8, giving us an actual time complexity of O(1)
# so, the total complexity would be O(log n) + O(1) -> O(log n)

# example usages
A = [5, 2, 4, 6, 8, 12, 24, 18, 23, 7, 3, 1, 9]
print(A)
print(Algo(A, len(A)))
print(tenth_largest(A, 0, len(A)-1, len(A)))
B = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
print(find_instances(B, len(B), 5))