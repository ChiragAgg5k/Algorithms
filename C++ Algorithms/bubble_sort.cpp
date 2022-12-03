#include <iostream>
using namespace std;

/// @brief Bubble Sort Algorithm implementation in C++
/// @param arr Array of integers to be sorted
/// @param size Size of the array
void bubbleSort(int arr[], int size)
{
    while (true)
    {

        bool swapped = false;

        for (int i = 0; i < size - 1; i++)
        {
            if (arr[i] > arr[i + 1])
            {

                swapped = true;

                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }

        if (!swapped)
        {
            break;
        }
    }
}

int main()
{

    int arr[] = {34, 121, 454, 22, 214, 54};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);

    cout << "Sorted array: ";

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    cout << endl;
    return 0;
}
