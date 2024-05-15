import math
import random


class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children


def generate_random_tree(depth):
    if depth == 0:
        value = random.randint(1, 10)
        print("Random value taken:", value)
        return Node(value=value)

    children = []
    for _ in range(random.randint(1, 3)):
        child = generate_random_tree(depth - 1)
        children.append(child)

    return Node(children=children)


def minimax(node, depth, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


depth = 3
tree = generate_random_tree(depth)

result = minimax(tree, depth, True)
print("The Optimal Value is:", result)