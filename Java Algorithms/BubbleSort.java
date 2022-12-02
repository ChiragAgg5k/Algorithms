import java.util.Scanner;
import java.util.Arrays;

public class BubbleSort {

  public static final Scanner scan = new Scanner(System.in);

  public static void main(String[] args) {

    System.out.print("Enter size of the array: ");
    int length = scan.nextInt();
    System.out.println();

    int[] testArray = new int[length];

    for (int i = 0; i < length; i++) {
      System.out.print("Enter element number " + (i + 1) + ": ");
      testArray[i] = scan.nextInt();
    }

    bubbleSort(testArray);

    System.out.println();
    System.out.print("Sorted array: " + Arrays.toString(testArray));

  }

  /**
   * Bubble Sort Algorithm implementation in Java.
   */
  public static void bubbleSort(int[] array) {

    // infinite loop , similar to while(true)
    for (;;) {

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
