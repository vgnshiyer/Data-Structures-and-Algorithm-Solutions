'''
Pay attention to the way the envelopes are sorted. 
We sort the envelopes greedily by width, and then by height in descending order.
'''
def maxEnvelopes(envelopes: List[List[int]]) -> int:
    n = len(envelopes)
    lis = []
    envelopes.sort(key = lambda x: (x[0], -x[1]))

    def bs(target):
        l, r = 0, len(lis)
        best = len(lis)
        while l < r:
            m = (l + r) >> 1
            if lis[m][0] < target[0] and lis[m][1] < target[1]: l = m + 1
            else: 
                best = m
                r = m
        return best

    for e in envelopes:
        index = bs(e)
        if index == len(lis): lis.append(e)
        else: lis[index] = e
    return len(lis)