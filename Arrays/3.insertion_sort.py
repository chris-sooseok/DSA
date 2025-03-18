"""
Best Runtime: O(n^2)
Worst Runtime: O(n^2)

Runtime Details:
while loop : O(n)
Finding insertion index: O(n(n-1) / 2)
Shifting for insertion : O(n - 1)
Overall: O(n^2)

Algorithm Idea:
For each iteration, find an index in where to insert the current value


"""

def insertion_sort(arr):

    n = len(arr)
    i = 0
    while i < n: # O(n)
        insert_idx = i
        elem = arr[insert_idx]

        for j in range(i, -1, -1): # O(n(n-1) / 2)
            if arr[j] > elem:
                insert_idx = j

        for g in range(i, insert_idx, -1): # O(n-1)
            arr[g] = arr[g-1]

        arr[insert_idx] = elem
        i +=1

    return arr


if __name__=="__main__":
   array = [7, 12, 9, 3, 11]
   array = insertion_sort(array)
   print(array)
