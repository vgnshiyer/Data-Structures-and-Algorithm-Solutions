'''
Whenever there is a sort of dependency between nodes in a graph, think about topologically sorting them.
'''
def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    recipe_book = {}
    for i, item in enumerate(recipes):
        recipe_book[item] = ingredients[i]

    being_prepared = set()
    @cache
    def search(item):
        if item in supplies: return True # found an item
        if item not in recipe_book: return False # raw material : must need
        being_prepared.add(item)
        for more_item in recipe_book[item]:
            if more_item in being_prepared: return False
            if not search(more_item): return False
        being_prepared.remove(item)
        return True

    can_make = []
    for item in recipes:
        if search(item): can_make.append(item)
    return can_make