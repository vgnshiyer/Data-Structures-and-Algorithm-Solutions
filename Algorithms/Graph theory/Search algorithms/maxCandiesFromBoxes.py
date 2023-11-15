def maxCandies(status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    n = len(status)
    boxes_found = set(initialBoxes)
    keys_found = set([i for i in range(n) if status[i]])
    opened = set()
    c = 0

    def dfs(box):
        opened.add(box)
        nonlocal c
        c += candies[box]

        for key in keys[box]:
            if key not in opened and key in boxes_found: dfs(key)
            keys_found.add(key)

        for innerBox in containedBoxes[box]:
            if innerBox not in opened and innerBox in keys_found: dfs(innerBox)
            boxes_found.add(innerBox)

    for box in initialBoxes: 
        if box not in opened and box in keys_found: 
            dfs(box)

    return c

def maxCandies(status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    boxes = set(initialBoxes)
    bfs = [i for i in boxes if status[i]]
    for i in bfs:
        for j in containedBoxes[i]:
            boxes.add(j)
            if status[j]: bfs.append(j)

        for j in keys[i]:
            if status[j] == 0 and j in boxes: bfs.append(j)
            status[j] = 1

    return sum(candies[i] for i in bfs)