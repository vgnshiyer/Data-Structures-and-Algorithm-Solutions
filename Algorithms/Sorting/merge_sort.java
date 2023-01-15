public class merge_sort {
    public static void conquer(int arr[], int l, int m, int h){
        System.out.println("Current Range : "+l+" "+m+" "+h);
        int temp[] = new int[h - l + 1];
        int x = 0;

        int i1 = l, i2 = m+1;
        while(i1 <= m && i2 <= h){
            if(arr[i1] <= arr[i2]) temp[x++] = arr[i1++];
            else temp[x++] = arr[i2++];
        }

        while(i1 <= m) temp[x++] = arr[i1++];
        while(i2 <= h) temp[x++] = arr[i2++];

        for(int i = 0, j = l; i < temp.length; i++, j++){
            arr[j] = temp[i];
        }

        System.out.println("Conquered : ");
        for(int i = l; i <= h; i++) System.out.print(arr[i]+" ");
        System.out.println();
    }

    public static void divide(int arr[], int l, int h){
        if(l >= h) return;

        int m = l + (h - l) / 2;
        divide(arr, l, m);
        divide(arr, m+1, h);

        conquer(arr, l, m, h);
    }

    public static void main(String args[]) {
        int arr[] = {12, 45, 8, 5, 16};
        int n = arr.length;

        System.out.println("Array before sorting..");
        for(int x : arr) System.out.print(x+" ");
        System.out.println();

        System.out.println("\nMerge Sort Visualization : ");
        divide(arr, 0, n-1);
        System.out.println();
        
        System.out.println("Array after sorting..");
        for(int x : arr) System.out.print(x+" ");
        System.out.println();
    }
}