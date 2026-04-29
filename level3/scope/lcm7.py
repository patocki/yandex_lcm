trees = []


def forest(tree: str):
    global trees
    count = trees.count(tree)
    trees.append(tree)
    return count
