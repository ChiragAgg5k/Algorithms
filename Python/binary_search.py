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
    r = len(arr) - 1

    while left <= r:
        m = (left + r) // 2
        if arr[m] > target:
            r = m - 1
        elif arr[m] < target:
            left = m + 1
        else:
            return m
    return -1


if __name__ == "main":
    testArray = list(
        map(int, input("Enter space separated array of integers: ").split())
    )
    target = int(input())

    # binary search requires the array to be sorted
    testArray.sort()

    print(f"{binary_search(arr=testArray,target=target)}th index.")
