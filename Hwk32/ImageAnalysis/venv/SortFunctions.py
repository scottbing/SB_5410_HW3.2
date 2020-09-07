import random

# Iterative mergesort function to
# sort arr[0...n-1]
def mergeSort(a, compare):
    current_size = 1

    # Outer loop for traversing Each
    # sub array of current_size
    while current_size < len(a) - 1:

        left = 0
        # Inner loop for merge call
        # in a sub array
        # Each complete Iteration sorts
        # the iterating sub array
        while left < len(a) - 1:
            # mid index = left index of
            # sub array + current sub
            # array size - 1
            mid = min((left + current_size - 1), (len(a) - 1))

            # (False result,True result)
            # [Condition] Can use current_size
            # if 2 * current_size < len(a)-1
            # else len(a)-1
            right = ((2 * current_size + left - 1,
                      len(a) - 1)[2 * current_size
                                  + left - 1 > len(a) - 1])

            # Merge call for each sub array
            merge(a, left, mid, right, compare)
            left = left + current_size * 2

        # Increasing sub array size by
        # multiple of 2
        current_size = 2 * current_size

    # Merge Function


def merge(a, l, m, r, compare):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if compare(L[i], R[j]):
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high, compare):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        #if arr[j] < pivot:
        if compare(pivot, arr[j]):
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSortRecursion(arr, low, high, compare):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high, compare)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1, compare)
        quickSort(arr, pi + 1, high, compare)


# Recursive Python3 code to sort
# an array using selection sort

# Return minimum index
def minIndex(a, i, j):
    if i == j:
        return i

    # Find minimum of remaining elements
    k = minIndex(a, i + 1, j)

    # Return minimum of current
    # and remaining.
    return (i if a[i] < a[k] else k)


# Recursive selection sort. n is
# size of a[] and index is index of
# starting element.
def recurSelectionSort(a, n, index=0):
    # Return when starting and
    # size are same
    if index == n:
        return -1

    # calling minimum index function
    # for minimum index
    k = minIndex(a, index, n - 1)

    # Swapping when index and minimum
    # index are not same
    if k != index:
        a[k], a[index] = a[index], a[k]

    # Recursively calling selection
    # sort function
    recurSelectionSort(a, n, index + 1)


def selectionSort(A, compare):
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if compare(A[min_idx], A[j]):
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]


# This function takes last element as pivot and places

# end of def selectionSort(A, compare):


# def selection_sort(array, compare):
#     # taken from:
#     # https://big-o.io/algorithms/comparison/selection-sort/
#     #print("in selectionsort: ", array)
#     # step 1: loop from the beginning of the array to the second to last item
#     currentIndex = 0
#     while (currentIndex < len(array) - 1):
#         # step 2: save a copy of the currentIndex
#         minIndex = currentIndex
#         # step 3: loop through all indexes that proceed the currentIndex
#         i = currentIndex + 1
#         while (i < len(array)):
#             # step 4:   if the value of the index of the current loop is less
#             #           than the value of the item at minIndex, update minIndex
#             #           with the new lowest value index
#             if (array[i] < array[minIndex]):
#                 # update minIndex with the new lowest value index
#                 minIndex = i
#             i += 1
#         # step 5: if minIndex has been updated, swap the values at minIndex and currentIndex
#         if (minIndex != currentIndex):
#             temp = array[currentIndex]
#             array[currentIndex] = array[minIndex]
#             array[minIndex] = temp
#         currentIndex += 1
#
#     return array
#
# #end of selection_sort(array, compare):

def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]


# end def comparePixels(pix1,pix2):


if __name__ == "__main__":
    # main()
    # two made up pixel tupelsa with rgb, xy
    px1 = ((255, 32, 12), (0, 10))
    px2 = ((128, 255, 255), (132, 12))
    pxls = [px1, px2]

    selectionSort(pxls, comparePixels)

    print(pxls)
