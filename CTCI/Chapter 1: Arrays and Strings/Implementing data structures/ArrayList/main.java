
import java.util.*;

public class main {
    
    public static void main(String[] args){
        MyArrayList<Integer> list = new MyArrayList<Integer>();

        list.add(1);
        list.add(2);
        list.add(3);

        int n = list.size();
        for(int i = 0; i < n; i++){
            System.out.print(list.get(i) + " ");
        }

        System.out.println("\nElement at index 0: " + list.get(0));
    }
}
