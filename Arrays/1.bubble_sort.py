"""
Best Runtime: O(n)
Time Complexity: O(n^2)

Runtime Details:
While loop: O(n)
Swapping: O(n(n-1) / 2)
Overall: O(n^2)

Best runtime occurs when the array is already sorted.
If the array is already sorted, no swapping occurs at all.
Therefore, we conclude it is sorted.

Algorithm Idea:
For every iteration, push the maximum value to the right most
Iterate until the array is all sorted
"""
def bubble_sort(arr):

    n = len(arr)
    i = 0

    while i < n: # O(n)
        swap_occured = 0
        for j in range(n-i-1): # O(n(n-1) / 2)
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

        # if no swap occurred at all, the arr is sorted
        if swap_occured == 0:
            break
        i+=1

    return arr

if __name__ == "__main__":

    array = [64, 34, 25, 12, 22, 11, 90, 5]
    array = bubble_sort(array)
    print(array)
    sorted_arr = [5, 11, 12, 22, 25, 34, 64, 90]
    sorted_arr = bubble_sort(sorted_arr)
    print(sorted_arr)