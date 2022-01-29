# possibly the simplest but dumbest and highly inefficient sorting algo

def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):  # size minus 1 as last position is already sorted
        swapped = False  # just trying to make the algo slightly more efficient by checking if anything is already sorted, we don't swap it again
        for j in range(size-1-i):  # when loop already run a few times, last portion is already sorted so ignore it, don't re-sort
            if elements[j] > elements[j+1]:  # if first element is greater than second one
                """
                tmp = elements[j]  # nooby way of swapping in other languages
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                """
                elements[j], elements[j + 1] = elements[j + 1], elements[j]  # the mighty python way of swapping in single line
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mary", "gina", "alex", "choi", "tamara"]

    bubble_sort(elements)
    print(elements)