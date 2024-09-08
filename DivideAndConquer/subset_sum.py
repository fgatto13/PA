def max_crossing_sum(A, left, mid, right):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, left-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
    
    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, right + 1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
    
    return left_sum + right_sum

def max_subarray_sum(A, left, right):
    if left == right:
        return A[left]
    
    mid = (left + right) // 2
    
    left_sum = max_subarray_sum(A, left, mid)
    right_sum = max_subarray_sum(A, mid+1, right)
    cross_sum = max_crossing_sum(A, left, mid, right)
    
    return max(left_sum, right_sum, cross_sum)

# Example usage
A = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(A, 0, len(A)-1))