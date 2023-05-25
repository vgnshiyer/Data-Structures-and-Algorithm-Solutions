def powerSet(arr: list, powerset: list, subset: list, index: int) -> None:
    if index >= len(arr):
        powerset.append(subset)
        return

    powerSet(arr, powerset, subset + [arr[index]], index + 1) ## include
    powerSet(arr, powerset, subset, index + 1) ## exclude 

def powerSet2(arr: list) -> list:
    powerset = []
    mx = 1 << len(arr)
    for i in range(mx):
        subset = getSubset(arr, i)
        powerset.append(subset)
    return powerset

def getSubset(arr: list, x: int) -> list:
    subset = []
    for k in range(len(arr)):
        if x & (1 << k):
            subset.append(arr[k])

    '''
    can also write like
    index = 0
    while(k):
        if k & 1: subset.append(arr[index])
        k >>= 1
        index += 1
    '''
    return subset

if __name__ == '__main__':
    powerset = []
    powerSet([1,2,3], powerset, [], 0)
    print(powerset)

    print(powerSet2([1,2,3]))