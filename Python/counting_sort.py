from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """Counting Sort algorithm implementation in python

    Time Complexity: O(log(n))
    Space Complexity: O(log(n+k)) , where k is the range of elements

    Args:
        arr (List[int]): Array of elements to be sorted.\n
        *Note* : The array must be have any number larger than 9

    Returns:
        List[int]: Sorted array
    """

    c = [0] * 10

    for i in range(len(arr)):
        c[arr[i]] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    i = len(arr) - 1
    res = [0] * len(arr)

    while i >= 0:
        res[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1
        i -= 1

    return res


if __name__ == "__main__":

    arr = list(map(int, input("Enter space separated array to be sorted: ").split()))
    print("Sorted array: ", counting_sort(arr))
