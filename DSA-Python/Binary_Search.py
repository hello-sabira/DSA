def binary_search_simple(arr, val):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] == val:
            found = True
        else:
            if val < arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1


def binary_search_recursive(arr, val):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr) // 2
        if arr[midpoint] == val:
            return True
        else:
            if val < arr[midpoint]:
                return binary_search_recursive(arr[:midpoint], val)
            else:
                return binary_search_recursive(arr[midpoint + 1:], val)
