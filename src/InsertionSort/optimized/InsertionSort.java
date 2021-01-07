package InsertionSort.optimized;

import java.util.Arrays;

public class InsertionSort {

    private InsertionSort() {
    }

    public static <E extends Comparable<E>> void sort(E[] arr) {

        for (int i = 0; i < arr.length; i++) {

            // 将 arr[i] 插入到合适的位置
//            for(int j = i; j - 1 >= 0; j --){
//                if(arr[j].compareTo(arr[j - 1]) < 0)
//                    swap(arr, j - 1, j);
//                else break;
//            }

            for (int j = i; j - 1 >= 0 && arr[j].compareTo(arr[j - 1]) < 0; j--)
                swap(arr, j - 1, j);
        }
    }

    public static <E extends Comparable<E>> void sort2(E[] arr) {

        for (int i = 0; i < arr.length; i++) { //[0,n)
            System.out.println("i" + i);
            // 将 arr[i] 插入到合适的位置
            E t = arr[i];
            int j;
            for (j = i; j - 1 >= 0; j--) { // [0,i]
                System.out.println("j" + j);
                if (t.compareTo(arr[j - 1]) < 0) {
                    arr[j] = arr[j - 1];
                } else {
                    break;
                }

            }
            System.out.println("change_j" + j);
            for (int x=0; x < arr.length; x++){
                System.out.print(arr[x]+",");
            }
            System.out.println("");
            arr[j] = t;
            System.out.println("end_arr");
            for (int x=0; x < arr.length; x++){
                System.out.print(arr[x]+",");
            }
            System.out.println("");
        }
    }

    private static <E> void swap(E[] arr, int i, int j) {

        E t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    private static <E extends Comparable<E>> boolean isSorted(E[] arr) {

        for (int i = 1; i < arr.length; i++)
            if (arr[i - 1].compareTo(arr[i]) > 0)
                return false;
        return true;
    }

    public static void main(String[] args) {

//        int[] dataSize = {10000, 100000};
        int[] dataSize = {10000};
        for (int n : dataSize) {
            Integer[] arr = ArrayGenerator.generateRandomArray(n, n);
            Integer[] arr2 = Arrays.copyOf(arr, arr.length);

            Integer[] arrTest = {2, 4, 6, 3, 1, 5};
            InsertionSort.sort2(arrTest);
            for (int x=0; x < arrTest.length; x++){
                System.out.print(arrTest[x]+",");
            }
//            SortingHelper.sortTest("InsertionSort", arr);
//            SortingHelper.sortTest("InsertionSort2", arrTest);
        }
        /**
         * InsertionSort , n = 10000 : 0.180320 s
         * InsertionSort2 , n = 10000 : 0.146157 s
         * InsertionSort , n = 100000 : 17.242725 s
         * InsertionSort2 , n = 100000 : 11.551383 s
         */
    }
}
