#include <iostream>
using namespace std;

/**
 * Insertion Sort Algorithm,
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
 *
 * @param arr[] array to be sorted
 * @param size size of array
 * @return void, in-place sorting
 */
void insertionSort(int arr[], int size)
{
    for (int i = 1; i < size; i++)
    {
        int j = i;
        while (arr[j] < arr[j - 1] and j > 0)
        {
            int temp = arr[j - 1];
            arr[j - 1] = arr[j];
            arr[j] = temp;
            j--;
        }
    }
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

    insertionSort(testArray, size);

    cout << "Sorted array: ";
    for (int i = 0; i < size; i++)
    {
        cout << testArray[i] << " ";
    }

    cout << endl;
}