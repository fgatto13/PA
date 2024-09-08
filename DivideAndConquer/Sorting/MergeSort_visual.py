import time

def wait(seconds=0.5):
    """Pause the execution for a given number of seconds."""
    time.sleep(seconds)

def MergeSort(A, left, right, depth=0):
    indent = '  ' * depth  # Create indentation based on recursion depth
    if left < right:
        mid = left + (right - left) // 2  # Determine the middle position
        print(f"{indent}MergeSort called on A[{left}:{mid}] -> {A[left:mid + 1]}")  # Print left subarray
        wait()  # Pause before recursive call
        MergeSort(A, left, mid, depth + 1)  # Sort the left half
        print(f"{indent}MergeSort called on A[{mid + 1}:{right}] -> {A[mid + 1:right + 1]}")  # Print right subarray
        wait()  # Pause before recursive call
        MergeSort(A, mid + 1, right, depth + 1)  # Sort the right half
        print(f"{indent}Before merging A[{left}:{right}] -> {A[left:right + 1]}")  # Print the array before merging
        wait()  # Pause before merging
        Merge(A, left, mid, right, depth)  # Merge the two halves
        print(f"{indent}After merging A[{left}:{right}] -> {A[left:right + 1]}")  # Print the array after merging
        wait()  # Pause after merging

def Merge(A, left, mid, right, depth):
    indent = '  ' * depth  # Create indentation based on recursion depth
    i = left  # Index of the left subarray (from left to mid)
    j = mid + 1  # Index of the right subarray (from mid + 1 to right)
    B = []  # Temporary array

    print(f"{indent}Merging left: {A[left:mid + 1]} and right: {A[mid + 1:right + 1]}") 
    wait()  # Pause before merging process starts

    while i <= mid and j <= right:  # It checks that i (starting from left) is less than or equal to mid, and j (starting from mid + 1) is less than or equal to right
        print(f"{indent}{A[i]} is less than or equal to {A[j]}? {A[i] <= A[j]}")  # Debug statement
        if A[i] <= A[j]:  # Checks if the element in A[i] is less than or equal to A[j]
            B.append(A[i])  # If true, the element gets inserted in the temporary array B (sequentially, remember to write k as the temporary index in the pseudocode)
            i += 1  # Increments the value of the index for the left subarray
        else:  # A[i] > A[j]
            B.append(A[j])  # Insert A[j] in the k position of B (the next position available in B)
            j += 1  # Increment the value of the right index
        print(f"{indent}Intermediate merged list: {B}")
        wait()  # Pause after each comparison

    # Since we exited the loop, this means that either i = mid or j = right, so in one of the two subarrays there is nothing more to append
    while i <= mid:  # This checks if there are any elements left in the left subarray
        B.append(A[i])  # If that's the case, inserts the element A[i] in B and increments i until there are no more elements
        i += 1
    
    while j <= right:  # Here it checks if there are any elements left in the right subarray
        B.append(A[j])  # If so, it inserts the one at the j position in B and increments j until there are no more elements
        j += 1

    # Remember that only one of these two loops will be executed, because in the previous main loop, either i = mid or j = right
    # Now that we've determined the subarray, we'll insert it in A starting from 0 to the size of B
    for k in range(len(B)):
        A[left + k] = B[k]
    
    print(f"{indent}Result of merging: {B} into A[{left}:{right}] -> {A[left:right + 1]}")  # Print the result of merging
    wait()  # Pause after completing the merge