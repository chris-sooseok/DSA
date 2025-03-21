
def merge_sort(array):
    
    n = len(array)

    if n <= 1:
        return array

    pivot = n // 2

    left = array[:pivot]
    right = array[pivot:]

    left_merge = merge_sort(left)
    right_merge = merge_sort(right)

    left_n = len(left_merge)
    right_n = len(right_merge)

    i = j = 0

    res = []

    while i < left_n and j < right_n:
        if left_merge[i] < right_merge[j]:
            res.append(left_merge[i])
            i += 1
        else:
            res.append(right_merge[j])
            j += 1

    # whatever the left value is, that is the highest value
    res.extend(left_merge[i:])
    res.extend(right_merge[j:])

    return res

if __name__ == "__main__":

    arr = [12, 8, 9, 3, 11, 5, 4]
    
    arr = merge_sort(arr)
    
    print(arr)