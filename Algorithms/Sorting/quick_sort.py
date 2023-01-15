def partition(arr, l, h):
    pivot = arr[h] ## choosing pivot as the last element
    i = l

    for j in range(l, h):
        if(arr[j] <= pivot):
            arr[i], arr[j] = arr[j], arr[i] ## place smaller element to the left of pivot
            i += 1
    arr[i], arr[h] = arr[h], arr[i]
    print("Partition for range "+str(l)+"-"+str(h)+":")
    print(arr)
    print("pivot at idx : "+str(i))
    return i  ## position of our pivot

def QuickSort(arr, l, h):
    if(l >= h): return
    pivot_idx = partition(arr, l, h)

    QuickSort(arr, l, pivot_idx-1)
    QuickSort(arr, pivot_idx+1, h)

if __name__ == "__main__":
    arr = [12, 45, 8, 5, 16]
    n = len(arr)

    print("Array before sorting..")
    print(arr)

    QuickSort(arr, 0, n-1)

    print("Array after sorting..")
    print(arr)
