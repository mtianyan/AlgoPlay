package InsertionSort.features;

import java.util.Arrays;

public class InsertionSort {

    private InsertionSort(){}

    public static <E extends Comparable<E>> void sort(E[] arr){

        for(int i = 0; i < arr.length; i ++){

            // 将 arr[i] 插入到合适的位置
            E t = arr[i];
            int j;
            for(j = i; j - 1 >= 0 && t.compareTo(arr[j - 1]) < 0; j --){
                arr[j] = arr[j - 1];
            }
            arr[j] = t;
        }
    }

    private static <E extends Comparable<E>> boolean isSorted(E[] arr){

        for(int i = 1; i < arr.length; i ++)
            if(arr[i - 1].compareTo(arr[i]) > 0)
                return false;
        return true;
    }

    public static void main(String[] args){

        int[] dataSize = {10000, 100000};
        for(int n: dataSize){

            System.out.println("Random Array : ");

            Integer[] arr = ArrayGenerator.generateRandomArray(n, n);
            Integer[] arr2 = Arrays.copyOf(arr, arr.length);
            SortingHelper.sortTest("InsertionSort", arr);
            SortingHelper.sortTest("SelectionSort", arr2);

            System.out.println();

            System.out.println("Ordered Array : ");

            arr = ArrayGenerator.generateOrderedArray(n);
            arr2 = Arrays.copyOf(arr, arr.length);
            SortingHelper.sortTest("InsertionSort", arr);
            SortingHelper.sortTest("SelectionSort", arr2);

            System.out.println();
            /**
             * Random Array :
             * InsertionSort , n = 10000 : 0.170421 s
             * SelectionSort , n = 10000 : 0.111151 s
             *
             * Ordered Array :
             * InsertionSort , n = 10000 : 0.000144 s
             * SelectionSort , n = 10000 : 0.106255 s
             *
             * Random Array :
             * InsertionSort , n = 100000 : 10.850796 s
             * SelectionSort , n = 100000 : 9.702210 s
             *
             * Ordered Array :
             * InsertionSort , n = 100000 : 0.000536 s
             * SelectionSort , n = 100000 : 7.439078 s
             */
        }
    }
}
