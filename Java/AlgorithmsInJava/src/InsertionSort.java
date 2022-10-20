import java.util.Arrays;

public class InsertionSort {

    public static void main(String[] args) {
        int[] testArray = { 6, 4, 2, 0, 1, 100, 20, 67, 42 };
        insertionSort(testArray);
        System.out.println(Arrays.toString(testArray));
    }

    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {

            // separate pointer     
            int j = i;

            while (j > 0 && (arr[j - 1] > arr[j])) {

                // swapping values 
                int temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;

                j--;

            }
        }
    }

}
