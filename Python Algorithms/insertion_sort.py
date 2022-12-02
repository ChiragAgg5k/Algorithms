from typing import List


def insertion_sort(arr: List[int]) -> None:
    """Insertion Sort algorithm implementation in python

    Time complexity : O(n^2)
    Space complexity : O(1)

    Args:
        List[int] : array to be sorted
    Returns:
        None : inplace function
    """

    for i in range(1, len(arr)):

        j = i

        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


if __name__ == "__main__":
    test_array = list(
        map(int, input("Enter space separated array to be sorted: ").split())
    )
    insertion_sort(test_array)  # inplace sort
    print("Sorted array:", test_array)
