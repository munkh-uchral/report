from typing import List

def recursiveInsertionSort(arr: List[int], n: int) -> None:
	# Base case: if the array has only one element, it is already sorted
	if n <= 1:
		return

	# Sort the first n-1 elements of the array recursively
	recursiveInsertionSort(arr, n - 1)

	# Insert the nth element into its correct position in the sorted subarray
	last = arr[n - 1]
	j = n - 2

	# Shift elements to the right to make space for the nth element
	while j >= 0 and arr[j] > last:
		arr[j + 1] = arr[j]
		j -= 1

	# Place the nth element in its correct position
	arr[j + 1] = last

def printArray(arr: List[int], n: int) -> None:
	for i in range(n):
		print(arr[i], end=" ")
	print()

arr = [99,76,4,21,35,34,45,53,94,25,31,42,9,5,60,67,64,33,1,66]
n = len(arr)

recursiveInsertionSort(arr, n)
printArray(arr, n)
