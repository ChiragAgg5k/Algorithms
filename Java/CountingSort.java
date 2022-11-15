import java.util.Arrays;

public class CountingSort {
    public static void main(String[] args) {
        int[] testArray = {9,8,7,6,5,4,3,2,1};
        int[] sortedArray = countingSort(testArray);
        System.out.println(Arrays.toString(sortedArray));
        
    }

    public static int[] countingSort(int[] arr){
        int[] count = new int[10];

        for (int j : arr) {
            count[j] += 1;
        }
        
        for(int i = 1 ; i<10 ; i++){
            count[i] += count[i-1];
        }

        int i = arr.length -1;

        int[] res = new int[arr.length];

        while(i>=0){
            res[count[arr[i]]-1] = arr[i];

            count[arr[i]] -= 1;
            i--;
        }

        return res;

    } 
}
