from BinarySearch import BinarySearch
from MergeSort_visual import MergeSort

A = []
while True:
    A.append(int(input("insert an element in A: ")))
    res = input("wanna add another? Y/N: ").upper()
    if res == 'N':
        break
print("Initial array:", A)
print("sorting the array:")
MergeSort(A, 0, len(A)-1)
print("Sorted array:", A)
c = int(input("which element do you want to find? "))
ind = BinarySearch(A, 0, len(A)-1, c)
if ind == -1:
    print("element not found")
else:
    print(f"element {c} found at position {ind}")