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