# 1- divide and conquer
# 2- done recursively
# 3-  time complexity of O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:  # base condition, whenever we have array of size one we exit
        return

    mid = len(arr) // 2  # double slash to indicate integer division

    left = arr[:mid]  # left is array uptill mid
    right = arr[mid:]  # right is mid till length of list (not included)

    merge_sort(left)  # recursive merge sort call on both mini lists
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    # arr is sorted merged list where we'll upload stuff, doing it in the same array to improve space complexity

    i = j = k = 0

    while i < len_a and j < len_b:  # of course we don't wanna go beyond any one's length
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1  # only move the pointer of the list from which you inserted an element
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    """
    we could also do this If a reached the end of list a add the remainder of b to sorted_list, and vice n versa 
    if i == len_a:
        sorted_list += b[j:]
    else:
        sorted_list += a[i:]
    but performance is same in backend
    """
    while i < len_a:  # if we stopped till previous while loop then the greater length list's remaining elements won't be sorted
        arr[k] = a[i]  # so these two while loops are necessary
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)
