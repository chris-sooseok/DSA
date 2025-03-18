"""
Best Runtime: O(nlogn)
Worst Runtime: O(n^2)

Details:
Iterating Array: O(n)
Partitioning: O(logn)

Algorithm Idea:
Partition the array based on pivot point
Smaller values to the left
Larger values to the right
"""

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    n = len(arr)
    partition = n // 2

    pivot = arr[partition]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__=="__main__":
   array = [7, 12, 9, 9, 9, 3, 11]
   array = quick_sort(array)
   print(array)
