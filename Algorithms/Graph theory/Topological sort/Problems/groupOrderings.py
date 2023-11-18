def sortItems(n: int, m: int, group: List[int], before: List[List[int]]) -> List[int]:
    group_graph = defaultdict(set)
    item_graph = defaultdict(set)
    item_to_group = [0] * n

    # g will be the new number of groups
    g = m
    # items not belonging to any group are assigned an invidivual group
    for i in range(n):
        if group[i] == -1:
            group[i] = g
            g += 1
        # mapping item to group
        item_to_group[i] = group[i]
    
    # building item and group graph
    for i in range(n):
        for j in before[i]:
            # item dependency
            item_graph[j].add(i)
            # group dependency
            if group[i] != group[j]:
                group_graph[group[j]].add(group[i])

    def top_sort(graph, n):
        indegree = [0] * n
        order = []

        for i in range(n):
            for j in graph[i]:
                indegree[j] += 1

        # starting nodes of the graph (indeg = 0)
        q = deque()
        for i in range(n):
            if indegree[i] == 0: q.append(i)

        while q:
            i = q.popleft()
            # all dependencies exhausted --> add to order
            order.append(i)
            for j in graph[i]:
                indegree[j] -= 1
                # add to queue if all dependencies were processed
                if indegree[j] == 0:
                    q.append(j)
        return order

    # form item orderings
    item_order = top_sort(item_graph, n)
    # found a circular dependency
    if len(item_order) != n: return []

    # form group orderings
    group_order = top_sort(group_graph, g)
    # found a circular dependency
    if len(group_order) != g: return []

    ans = []
    # storing in a map for faster lookup
    group_map = defaultdict(list)
    for item in item_order:
        group_map[item_to_group[item]].append(item)
    # building final item orderings
    for group in group_order:
        ans += group_map[group]
        
    return ans