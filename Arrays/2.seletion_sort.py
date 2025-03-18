"""
Best Runtime: O(n^2)
Worst Runtime: O(n^2)

Runtime Details:
While loop : O(n)
Finding minimum value: O(n(n-1) / 2)
Overall: O(n^2)

Algorithm Idea:
Find the minimum value through an iteration.
Locate the minimum value at the starting index of each range
"""
def selection_sort(arr):

    n = len(arr)
    i = 0
    while i < n: # O(n)
        min_idx = i
        for j in range(i, n): # O(n(n-1) / 2)
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        i += 1

    return arr

if __name__ == "__main__":

    array = [3, 12, 9, 11, 7]
    array = selection_sort(array)
    print(array)