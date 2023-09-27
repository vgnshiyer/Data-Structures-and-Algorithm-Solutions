def shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    '''
    Instead of iterating for a particular item, iterate over the shopping offers. Decide whether to buy the offer or not.
    '''
    @cache
    def dfs(i, items):
        if items == (0,) * len(items): return 0

        ans = 0
        for k, item in enumerate(items): ans += items[k] * price[k]

        for k in range(i, len(special)):
            offer = special[k]
            canBuy = True
            for j in range(len(items)):
                if items[j] < offer[j]:
                    canBuy = False
                    break
            if not canBuy: continue

            ans = min(ans, offer[-1] + dfs(k, tuple([n - s for n, s in zip(items, offer[:-1])])))
        return ans

    return dfs(0, tuple(needs))

def shoppingOffers_bitmask(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    def getMask(arr):
        mask = 0
        for x in arr:
            mask = (mask | x) << 4
        return mask

    @cache
    def dfs(i, mask):
        nonlocal needs
        if mask == 0: return 0

        ans = 0
        for k, n in enumerate(needs): ans += n * price[k]
        needs_copy = needs.copy()
        for k in range(i, len(special)):
            offer = special[k]
            canBuy = True
            for j in range(len(needs)):
                if needs[j] < offer[j]:
                    canBuy = False
                    break
            if not canBuy: continue
            newItems = [n - s for n, s in zip(needs, offer[:-1])]
            needs = newItems
            ans = min(ans, offer[-1] + dfs(k, getMask(newItems)))
            needs = needs_copy
        return ans

    return dfs(0, getMask(needs))