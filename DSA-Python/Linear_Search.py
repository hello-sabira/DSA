def LinearSearch(arr, val):
    for i in range(len(arr)):
        if val == arr(i):
            return i
    return -1


arr = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
x = 'a'
print("element found at index " + str(LinearSearch(arr, x)))
