def magicIndex(arr: list) -> int:
    l, r = 0, len(arr) - 1
    while(l < r):
        m = (l + r) >> 1
        if arr[m] <= m:
            l = m
        else: 
            r = m - 1
    return l if arr[l] == l else -1

def magicIndex2(arr: list, l: int, r: int) -> int:
    if l > r: return -1

    m = (l + r) >> 1
    if arr[m] == m: return m

    leftSearch = magicIndex2(arr, l, min(m-1, arr[m])) ## we take the minimum as any number before arr[m] must be less than m and cannot be the magic number. (eg. arr[m] = 3, m = 5 .. therefore arr[m-1] cannot be 4 as the array is sorted. So we skip to the index arr[m] directly)
    if leftSearch != -1: return leftSearch
    
    rightSearch = magicIndex2(arr, max(m+1, arr[m]), r) ## same for the right hand side
    return rightSearch


if __name__ == '__main__':
    inp = [-3, -2, -1, 1, 2, 3, 5, 7, 10, 11, 12] ## all distinct
    print(magicIndex(inp))

    inp2 = [-2, -1, 2, 2, 2, 3, 5, 7, 10, 11,12] ## with duplicates
    print(magicIndex2(inp2, 0, len(inp2)-1))
