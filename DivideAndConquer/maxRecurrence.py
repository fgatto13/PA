def MaxConsecutiveLength(A, left, right):
    if left == right:
        # Base case: single element
        return 1
    
    mid = (left + right) // 2
    
    # Recursively find the longest sequence in the left and right halves
    leftMax = MaxConsecutiveLength(A, left, mid)
    rightMax = MaxConsecutiveLength(A, mid + 1, right)
    
    # Combine step: find the longest sequence that crosses the middle
    # This involves counting consecutive elements from the middle to the left and from the middle+1 to the right
    
    # Count the consecutive elements to the left of mid
    leftPart = 0
    leftIndex = mid
    while leftIndex >= left and A[leftIndex] == A[mid]:
        leftPart += 1
        leftIndex -= 1
    
    # Count the consecutive elements to the right of mid
    rightPart = 0
    rightIndex = mid + 1
    while rightIndex <= right and A[rightIndex] == A[mid + 1]:
        rightPart += 1
        rightIndex += 1
    
    # If the elements on both sides of the midpoint are the same, combine the counts
    crossMax = 0
    if A[mid] == A[mid + 1]:
        crossMax = leftPart + rightPart
    
    # Return the maximum of the three possibilities
    return max(leftMax, rightMax, crossMax)

# Initial call
A = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]
print(MaxConsecutiveLength(A, 0, len(A) - 1))