import java.util.Arrays;

public class BubbleSort {

    public static void main(String[] args) {

        int[] testArray = {2, 45, 123, 5, 46, 2, 356, 7, 8, 3};
        System.out.println("Before: " + Arrays.toString(testArray));

        bubbleSort(testArray);
        System.out.println("After: " + Arrays.toString(testArray));
    }


    /**
     * Bubble Sort Algorithm implementation in Java.
     */
    public static void bubbleSort(int[] array) {

        // infinite loop , similar to while(true)
        for (; ; ) {

            boolean swapped = false;

            for (int i = 0; i < (array.length - 1); i++) {
                if (array[i] > array[i + 1]) {

                    swapped = true;

                    // traditional swap
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;
                }
            }

            // if no swaps take place , our array has been sorted
            if (!swapped) {
                break;
            }
        }
    }
}
