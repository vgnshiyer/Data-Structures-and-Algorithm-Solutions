## 1.5 One edit away

def isOneReplaceAway(word1, word2):
    foundDifference = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True

def isOneEditRemoveAway(smaller, larger):
    id1, id2 = 0, 0
    foundDifference = False

    while(id1 < len(smaller) and id2 < len(larger)):
        if smaller[id1] != larger[id2]:
            if foundDifference:
                return False
            id2 += 1
            foundDifference = True
        else:
            id1 += 1
            id2 += 1
    return True

def isOneEditAway(word1, word2) -> bool:
    if len(word1) == len(word2):
        return isOneReplaceAway(word1, word2)
    else:
        if abs(len(word1) - len(word2)) != 1:
            return False
        if len(word1) < len(word2):
            smaller = word1
            larger = word2
        else:
            smaller = word2
            larger = word1
        return isOneEditRemoveAway(smaller, larger)

if __name__ == '__main__':
    test_cases = [
        ['pale', 'plo'],
        ['pales', 'pale'],
        ['pale', 'bale'],
        ['pale', 'bake']
    ]

    for tc in test_cases:
        print(isOneEditAway(tc[0], tc[1]))