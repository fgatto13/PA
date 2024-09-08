def BinarySearch(A, left, right, c, depth=0) -> int:
    indent = '  ' * depth  # Create indentation based on the recursion depth
    if left > right:
        print(f"{indent}Not found")
        return -1

    mid = (right + left) // 2
    print(f"{indent}Move to position {mid}: {A[mid]}")
    print(f"{indent}Current array slice: {A[left:right+1]}")
    print(f"{indent}Is {A[mid]} equal to {c}? {A[mid] == c}")

    if A[mid] == c:
        return mid
    elif A[mid] > c:
        print(f"{indent}Is {A[mid]} greater than {c}? {A[mid] > c}")
        return BinarySearch(A, left, mid - 1, c, depth + 1)
    else:
        print(f"{indent}Is {A[mid]} less than {c}? {A[mid] < c}")
        return BinarySearch(A, mid + 1, right, c, depth + 1)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(BinarySearch(A, 0, len(A)-1, 3))
print(BinarySearch(A, 0, len(A)-1, 12))