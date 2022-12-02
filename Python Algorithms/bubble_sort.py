from typing import List


def bubble_sort(array: List[int]) -> None:
    """Bubble Sort algorithm implementation in python

    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        array (List[int]): Array of integers to be sorted
    """

    while True:

        swapped = False

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:

                # pythonic way to swap
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    testArray = list(
        map(
            int, input("Enter space separated array of integers to be sorted: ").split()
        )
    )
    bubble_sort(testArray)
    print("Sorted array =", testArray)
