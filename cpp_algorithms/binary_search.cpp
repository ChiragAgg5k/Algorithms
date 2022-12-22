#include <iostream>
using namespace std;

/**
 * @brief search algorithm.
 * Time complexity: O(log n),
 * Space complexity: O(1)
 *
 * @param arr[] array of integers to be searched
 * @param size size of array
 * @param key key to be searched
 * @return index of key if found, -1 otherwise
 */
int binarySearch(int arr[], int size, int key)
{

    int left = 0;
    int right = size - 1;

    while (left <= right)
    {

        int mid = (left + right) / 2;

        if (arr[mid] > key)
        {
            right = mid - 1;
        }
        else if (arr[mid] < key)
        {
            left = mid + 1;
        }
        else
        {
            return mid;
        }
    }

    return -1;
}

int main()
{
    int size;
    cout << "Enter size of the array: ";
    cin >> size;

    cout << "Enter space separated array of integers: ";
    int testArray[size];

    for (int i = 0; i < size; i++)
    {
        cin >> testArray[i];
    }

    int target;
    cout << "Enter target integer: ";
    cin >> target;

    int index = binarySearch(testArray, size, target);

    cout << "Index of the given target integer is: ";
    cout << index << endl;
}