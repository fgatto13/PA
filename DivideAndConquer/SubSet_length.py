def mid_sequence(A, mid, n):
    B = [A[mid]]
    i = mid-1
    while i >= 0 and A[mid] == A[i]:
        B.append(A[i])
        i -= 1
    i = mid+1
    while i < n and A[mid] == A[i]:
        B.append(A[i])
        i += 1
    return B

def max_recurr_subseq(A, left, right):
    if left > right:
        return []
    if left == right:
        return [A[left]]
    mid = (left + right) // 2
    leftSide = max_recurr_subseq(A, left, mid)
    rightSide = max_recurr_subseq(A, mid+1, right)
    midSide = mid_sequence(A, mid, len(A)-1)
    if len(midSide) >= len(leftSide) or len(midSide) >= len(rightSide):
        return midSide
    elif leftSide[0] == rightSide[0]:
        return leftSide + rightSide
    elif len(leftSide) > len(rightSide):
        return leftSide
    else:
        return rightSide
    
A = [1, 1, 1, 1, 1, 2, 5, 4, 6, 8, 5, 2, 2, 2, 2]
print(A)
print(max_recurr_subseq(A, 0, len(A)-1))