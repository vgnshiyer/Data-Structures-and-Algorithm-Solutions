## LRU Cache

**Caching** is a technique to store data in a faster storage (usually RAM) to serve future requests faster. 

Below are some common examples where cache is used:

* A processor cache is used to read data faster from main memory (RAM).
* Cache in RAM can be used to store part of disk data in RAM and serve future requests faster.
* Network responses can be cached in RAM to avoid too many network calls.

However, cache store is usually not big enough to store the full data set. So we need to evict data from the cache whenever it becomes full. There are a number of caching algorithms to implement a cache eviction policy. LRU is very simple and a commonly used algorithm. The core concept of the LRU algorithm is to evict the oldest data from the cache to accommodate more data.

Least Recently Used (LRU) is a common cache eviction strategy. It defines the policy to evict elements from the cache to make room for new elements when the cache is full, meaning it discards the least recently used items first.

Let’s take an example of a cache that has a capacity of 4 elements. We cache elements 1, 2, 3 and 4.

CACHE = {1, 2, 3, 4}

We now need to cache another element “5”.

CACHE = {2, 3, 4, 5}

In LRU cache, we evict the least recently used element (in this case “1”) in case a new element needs to be cached. Now “2” is next in line to be evicted if a new element needs to be cached. Let’s see what happens when “2” is accessed again.

CACHE = {3, 4, 5, 2}

Now “3” becomes the next in line to be evicted from the cache.

To implement an LRU cache we use two data structures: a hashmap and a doubly linked list. A doubly linked list helps in maintaining the eviction order and a hashmap helps with O(1) lookup of cached keys. Here goes the algorithm for LRU cache.
```
If the element exists in hashmap
    move the accessed element to the tail of the linked list
Otherwise,
    if eviction is needed i.e. cache is already full
        Remove the head element from doubly linked list and delete its hashmap entry
    Add the new element at the tail of linked list and in hashmap
Get from Cache and Return
```

Note that the doubly linked list is used to keep track of the most recently accessed elements. The element at the tail of the doubly linked list is the most recently accessed element. All newly inserted elements (in put) go the tail of the list. Similarly, any element accessed (in get operation) goes to the tail of the list.
