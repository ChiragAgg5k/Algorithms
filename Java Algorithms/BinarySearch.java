public class BinarySearch {

  public static void main(String[] args) {
    int[] testArray = { 1, 2, 3, 4, 5 };
    System.out.println(binary_search("Target is found at index: " + testArray, 3));
  }

  /**
   * Binary Search algorithm implementation in Java
   *
   */
  public static int binary_search(int[] arr, int target) {

    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {

      int mid = (left + right) / 2;

      if (arr[mid] > target) {
        right = mid - 1;
      } else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        return mid;
      }
    }
    return -1;
  }

}
