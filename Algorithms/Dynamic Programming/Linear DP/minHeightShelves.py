from functools import cache

def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    '''
    state: dp[i][j]-> min height of shelf at book i, with k as the max height of the books so far on a current row and j is the remaining width of the shelf
    transition: We can either decide to place the current book on the current row (provided that there is enough space available) or we can decide to place the current book on the next row

        place on current row:
            dp[i][j]= dp[i+1][j-book_thickness]
        place on next row:
            dp[i][j]= min(dp[i][j], k + dp[i+1][shelfWidth - book_thickness][book_height])
    '''

    @cache
    def helper(i, j, mx=0):
        if i == len(books): return mx
        
        book_thickness, book_height = books[i]

        place_on_current_shelf = place_on_next_shelf = 10 ** 6
        if j >= book_thickness:
            place_on_current_shelf = helper(i+1, j - book_thickness, max(mx, book_height))
        
        place_on_next_shelf = mx + helper(i+1, shelfWidth - book_thickness, book_height)

        return min(place_on_current_shelf, place_on_next_shelf)

    return helper(0, shelfWidth)

'''
Notice that the iterative version eliminates two variables from our state.
These type of problems where we are made to keep track of a max/min value between recursive calls can be simplified with some iterative tricks.
In this problem, we tried to greedily place books in a shelf while tracking the minimum height of the books placed so far.
Therefore there was no need to store that information. All we stored and want is, what is the minimum height of the books placed at position j.
'''
def minHeightShelves_iterative(books: List[List[int]], shelfWidth: int) -> int:
    dp = [float('inf')] * (len(books) + 1)
    dp[0] = 0

    for i in range(1, len(books) + 1):
        width, height = books[i - 1]
        dp[i] = dp[i - 1] + height ## place next book on the next shelf
        j = i - 1
        while j > 0 and (width + books[j - 1][0]) <= shelfWidth:
            height = max(height, books[j-1][1])
            width += books[j-1][0]
            dp[i] = min(dp[i], dp[j-1] + height)
            j -= 1
    return dp[-1]