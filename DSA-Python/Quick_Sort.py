# Best element to choose pivot where the list splits in half or choose the median
# Choosing random pivot may ensure O (n log n) performance
# Recursive function
# worst case O(n^2)
# best case O (n log n)
# in case of duplicate, 3 way quick sort: geeksforgeeks

def quicksort(arr):
    qs(arr, 0, len(arr) - 1)


def qs(arr, l, r):  # we're takig l and r as first and last element respectively
    if l >= r:  # of course, base condition first, since we're sorting elements between l and r, if l >= r it means list has already been sorted!
        return
    p = partition(arr, l,
                  r)  # goal of this function is to divide list in in to 2 groups, less than pivot and greater than pivot

    qs(arr, l, p - 1)  # recursively calling function to sort array b/w left partition to pivot
    qs(arr, p + 1, r)  # recursively calling function to sort array b/w pivot and right partition
    # note we'll get a new pivot p in each iteration


def partition(arr, l,
              r):  # 2 mega condition we always wanna satisfy, 1. all the numbers from beginning, upto i is always < pivot, 2. all the numbers b/w i and j is always >= pivot
    pivot = arr[r]  # choosing pivot as last element
    i = l - 1
    for j in range(l,
                   r):  # j will increment each loop, but j and i's value will only change when the below condition is true
        if arr[
            j] < pivot:  # we check this condition, as we always wanna satisfy the 2 mega condition, and when one/both aint satisfied, we carry out step a and b
            i += 1  # a
            arr[i], arr[j] = arr[j], arr[i]  # b
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1  # now that arr has been divided into 2 subgroups, value > p and < p, time to put p b/w these 2 groups by returning it as i + 1, sounds logical


a1 = [3, 2, 1]
a2 = [1, 2, 3]
a3 = []
a4 = [3, 1, -1, 0, 2, 5]
a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
a6 = [0]
a7 = [3, -2, -1, 0, 2, 4, 1]
a8 = [1, 2, 3, 4, 5, 6, 7]
a9 = [2, 2, 2, 2, 2, 2, 2]

quicksort(a1)
quicksort(a2)
quicksort(a3)
quicksort(a4)
quicksort(a5)
quicksort(a6)
quicksort(a7)
quicksort(a8)
quicksort(a9)

assert a1 == [1, 2, 3]
assert a2 == [1, 2, 3]
assert a3 == []
assert a4 == [-1, 0, 1, 2, 3, 5]
assert a5 == [0, 0, 1, 1, 2, 2, 2, 2, 2, 4, 4]
assert a6 == [0]
assert a7 == [-2, -1, 0, 1, 2, 3, 4]
assert a8 == [1, 2, 3, 4, 5, 6, 7]
assert a9 == [2, 2, 2, 2, 2, 2, 2]

print("If you didn't get an assertion error, this program has run successfully.")
