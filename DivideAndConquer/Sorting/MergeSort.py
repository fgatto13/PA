def MergeSort(A, left, right):
    if left < right:
        mid = left + (right - left)// 2
        MergeSort(A, left, mid)
        MergeSort(A, mid+1, right)
        Merge(A, left, mid, right)

def Merge(A, left, mid, right):
    # initialization
    i = left
    j = mid+1
    B = []

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    # checks for remaining elements either in the left or in the right position
    while i <= mid:
        B.append(A[i])
        i += 1
    while j <= right:
        B.append(A[j])
        j += 1
    for k in range(len(B)):
        A[left + k] = B[k]

Arr = [5, 4, 6, 8, 12, 10, 14, 18, 15, 13]
print("Initial array:", Arr)
MergeSort(Arr, 0, len(Arr) - 1)
print("Sorted array:", Arr)