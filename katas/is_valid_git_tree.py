def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise

    """
    all_nodes = set(tree_map.keys())
    child_nodes = set(child for children in tree_map.values() for child in children)
    roots = all_nodes - child_nodes

    if len(roots) != 1:
        return False

    root = next(iter(roots))
    visited = set()
    visiting = set()

    def dfs(node):
        if node in visiting:
            return False  # cycle
        if node in visited:
            return True

        visiting.add(node)
        for child in tree_map.get(node, []):
            if not dfs(child):
                return False
        visiting.remove(node)
        visited.add(node)
        return True

    if not dfs(root):
        return False

    return visited == all_nodes


if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False