from collections import *

inp = ['wrt','wrf','er','ett','rftt']

def findLetterOrder(words):
    adj = defaultdict(set)

    ## building the graph
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1),len(w2))

        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: return ''

        for k in range(minLen):
            if w1[k] != w2[k]:
                ## add adge
                adj[w1[k]].add(w2[k])
                break

    letterOrder = []

    def topSort(letter, visited, beingVisited):
        visited.add(letter)
        beingVisited.add(letter)

        for nextLetter in adj[letter]:
            if nextLetter in beingVisited: return '' ## detected a cycle 
            if nextLetter in visited: continue
            topSort(nextLetter, visited, beingVisited)
        
        beingVisited.remove(letter)
        letterOrder.append(letter)

    visited = set()
    for c in list(adj):
        if c not in visited: topSort(c, visited, set())

    return ''.join(letterOrder[::-1])

print(findLetterOrder(inp))