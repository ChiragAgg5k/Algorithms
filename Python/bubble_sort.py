def bubble_sort(array: list):

    # our "swapped" boolean variable checks if there has been atleast one swap in each iteration of the while loop
    # if not , then our array is sorted.

    while True:

        swapped = False

        for i in range(len(array)-1):
            if array[i] > array[i+1]:

                # pythonic way to swap
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    testArray = [1, 10, 5, 2, 3, 4, 6, 4, 7]
    bubble_sort(testArray)
    print(testArray)
