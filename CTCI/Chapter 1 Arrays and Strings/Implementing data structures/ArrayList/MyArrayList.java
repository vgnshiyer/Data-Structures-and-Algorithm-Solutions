import java.util.Arrays;

// reference: https://www.vogella.com/tutorials/JavaDatastructureList/article.html
public class MyArrayList<E>{
    private int size = 0;
    private static final int DEFAULT_CAPACITY = 10;
    private Object elements[];

    public MyArrayList(){
        elements = new Object[DEFAULT_CAPACITY];
    }

    public int size(){
        return size;
    }

    public void add(E e){
        if(size == elements.length){
            expand();
        }
        elements[size++] = e;
    }

    private void expand(){
        int newSize = elements.length * 2;
        elements = Arrays.copyOf(elements, newSize);
    }
    
    @SuppressWarnings("unchecked")
    public E get(int id){
        if(id > size || id < 0){
            throw new IndexOutOfBoundsException();
        }
        return (E) elements[id];
    }
}