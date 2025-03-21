"""
Runtime: O(logn)

Algorithm Idea:
Only works for sorted array
Compare target value with the middle point of array and cut the array half
"""
def binary_search(arr, val):

    left = 0
    right = len(arr) - 1

    while left != right:

        middle = (left + right) // 2

        if arr[middle] == val:
            return middle
        else:
            if val < arr[middle]:
                right = middle
            else:
                left = middle

    return -1



if __name__ == "__main__":
    arr = [2, 3, 7, 7, 11, 15, 25, 32, 45, 56, 60, 70, 85, 90, 95]

    idx = binary_search(arr, 2)
    print(idx)
