from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """Binary Search algorithm implementation in python

    Time Complexity: O(log(n))
    Space Complexity: O(1)

    Args:
        arr (List[int]): Sorted array of integers
        target (int): Target integer whose index is to be returned

    Returns:
        int: index of target integer
    """

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            return mid

    return -1


if __name__ == "__main__":

    # Make sure the entered array is sorted.
    testArray = list(
        map(int, input("Enter space separated array of integers: ").split())
    )
    target = int(input("Enter target integer: "))

    print(f"Index = {binary_search(arr=testArray,target=target)}")
