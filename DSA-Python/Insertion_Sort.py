# Faster than Bubble and Selection sort in small number of test cases
"""
Pseudo code for insertion sort
Insertion sort (a, n)
for i <- 1 to n-1
{
  value <- a[i]
  hole <- i
  while (hole > 0 && A[hole-1]>value) {
    A[hole] <- A[hole-1]
    hole <- hole - 1
    }
   A[hole] <- value
   }
}
"""
# https://www.youtube.com/watch?v=JU767SDMDvA for explanation


def insertion_sort(element_list):
    for index in range(1, len(element_list)):
        current_value = element_list[index]
        position = index
        while position > 0 and element_list[position - 1] > current_value:
            element_list[position] = element_list[position - 1]
            position = position - 1
        element_list[position] = current_value


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)
    #
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')
