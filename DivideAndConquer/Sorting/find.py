def Find (A, left, right, x) -> list:
    if left > right:
        return []
    mid = (left + right) // 2
    if x == A[mid]:
        l = []
        j = mid
        i = mid-1
        while A[j] == x and j < len(A):
            l.append(j)
            j += 1
        while A[i] == x and i > 0:
            l.append(i)
            i -= 1
        return sorted(l)
    elif x > A[mid]:
        return Find(A, mid+1, right, x)
    else:
        return Find(A, left, mid-1, x)

A = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9, 10]
print(Find(A, 0, len(A)-1, 2))
print(Find(A, 0, len(A)-1, 12))