def Trova(A, left, right, x):
    if left > right:
        return False
    mid = (left + right) // 2
    if A[mid] == x:
        return True
    else:
        leftSide = Trova(A, left, mid-1, x)
        rightSide = Trova(A, mid+1, right, x)
        return leftSide or rightSide
    
A = [14, 18, 10, 3, 4, 5, 75, 48, 34]
print(A)
print(Trova(A, 0, len(A)-1, 5))
print(Trova(A, 0, len(A)-1, 0))