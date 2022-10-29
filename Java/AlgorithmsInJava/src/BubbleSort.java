import java.util.Arrays;

public class BubbleSort {

    public static void main(String[] args) {

        int[] testArray = {5,4,7,8,4,2,1,45,7,8,43};
        bubbleSort(testArray);
        System.out.println(Arrays.toString(testArray));

    }

    public static void bubbleSort(int[] array){

        // infinite loop , similar to while(true)
        for(;;){

            boolean swapped = false;

            for(int i = 0; i < (array.length -1) ; i++){
                if(array[i] > array[i+1]){

                    swapped = true;

                    // traditional swap
                    int temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                }
            }

            // if no swaps take place , our array has been sorted
            if(!swapped){
                break;
            }
        }
    }
}
