'''
state: dp[i] -> set of unique ORs for all subarrays ending at i
transition: at every new element, we add a new set with itand add the OR of all the elements from the subset before it
base case: dp[i] = {arr[i]}
'''

def subarrayBitwiseORs(arr: List[int]) -> int:
    dp = [set([arr[i]]) for i in range(len(arr))]
    res = dp[0]

    for i in range(1, len(arr)):
        for prev in dp[i-1]:
            dp[i].add(arr[i] | prev)
        res |= dp[i]
    return len(res)

def subarrayBitwiseORs_spaceOptimized(arr: List[int]) -> int:
    dp = {arr[0]}
    res = dp

    for i in range(1, len(arr)):
        dp2 = {arr[i]}
        for prev in dp:
            dp2.add(arr[i] | prev)
        res |= dp2
        dp = dp2
    return len(res)

def subarrayBitwiseORs_spaceOptimized2(arr: List[int]) -> int:
    dp = {arr[0]}
    res = dp
    for i in range(1, len(arr)):
        dp = {x | arr[i] for x in dp} | {arr[i]}
        res |= dp
    return len(res)