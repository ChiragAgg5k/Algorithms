import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) throws Exception {

        int[] testArray = { 10, 2, 8, 3, 100, 53, 32, 57 };
        mergeSort(testArray);
        System.out.println(Arrays.toString(testArray));

    }

    // Overloaded
    public static void mergeSort(int[] arr) {
        mergeSort(arr, arr.length);
    }

    public static void mergeSort(int[] arr, int n) {
        if (n < 2) {
            return;
        }

        int mid = n / 2;
        int[] left = new int[mid];
        int[] right = new int[n - mid];

        for (int i = 0; i < mid; i++) {
            left[i] = arr[i];
        }

        for (int i = mid; i < n; i++) {
            right[i - mid] = arr[i];
        }

        mergeSort(left, mid);
        mergeSort(right, n - mid);

        int i = 0, j = 0, k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < left.length) {
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < right.length) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

}
