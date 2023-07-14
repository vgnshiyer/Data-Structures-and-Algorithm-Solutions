'''
You are given a string S. In one move you can erase from S a pair of identical letters. Find the shortest possible string that can be created this way. If there are many such strings, choose the alphabetically (lexicographically) smallest one. Note that there is no limit to the number of moves.

Write a function:
def solution (S)
that, given a string S of length N, returns the shortest string (or the first alphabetically, in the case of a draw) created by erasing pairs of identical letters from S.

Examples:
1. For S = "CBCAAXA" you can make, for example, two moves:
• first erase a pair of letters "c": "CBCAAXA" -* 'BAAXA";
• then erase a pair of letters "A". "BAAXA", "BAX™.
Thus the string "BAX" is created. There is no way to create a shorter string. The other string of length 3 that can be created is "BXA" but "BAy" is the first alphabetically. The function should return "BAX".
'''

## O(n) Time complexity, O(n) Space complexity
def solution(S):
    ## using monotonic stack to maintain increasing order of characters in string
    smallestPossibleString = []
    indices = {char: i for i, char in enumerate(S)}
    count = Counter(S)

    for i, char in enumerate(S):
        if char in smallestPossibleString or count[char] % 2 == 0: continue
        while smallestPossibleString and smallestPossibleString[-1] > char and i < indices[smallestPossibleString[-1]]: smallestPossibleString.pop()
        smallestPossibleString.append(char)
    return ''.join(smallestPossibleString)