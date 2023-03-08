public class MyHashMap<K, V> {
    private int CAPACITY = 10;
    private LinkedList<Pair> bucket[];
    private int size = 0;

    public MyHashMap(){
        this.bucket = new LinkedList[CAPACITY];
    }

    private int getHash(K key){
        return (key.hashCode() & 0xfffffff) % CAPACITY;
    }

    // public void put(K key, V value){
    //     if(containsKey(key)){
    //         Pair p = get
    //     }
    // }
}
