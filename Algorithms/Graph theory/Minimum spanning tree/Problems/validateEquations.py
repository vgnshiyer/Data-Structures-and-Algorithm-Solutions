def equationsPossible(equations: List[str]) -> bool:
    e, ne = [x for x in equations if x[1:-1] == '=='], [x for x in equations if x[1:-1] == '!=']

    parent = {}
    def find(a):
        if a not in parent: parent[a] = a
        if a != parent[a]:
            a = find(parent[a])
        return a

    def union(a, b):
        parent[find(b)] = find(a)

    '''
    Gather all '==' equations and unite them.
    Gather all '!=' equations and check if they are in the same set. (looking for cycles)
    a == b, b == c, c != a <- this is a cycle
    '''
    for eq in e:
        x, y = eq[0], eq[-1]
        if find(x) != find(y): union(x, y)

    for eq in ne:
        x, y = eq[0], eq[-1]
        if find(x) == find(y): return False
    return True