import itertools
from functools import reduce


class FdNode:
    def __init__(self, attr_list):
        self.attr_set = set(attr_list)


class Level:
    def __init__(self, n_level, alphabet, last_level):
        if n_level == 1:
            self.nodes = []
            for c in alphabet:
                self.nodes.append(FdNode([c]))
        else:
            self.nodes = generate_next_level(n_level, last_level)


def generate_next_level(n_level, last_level):
    candidates = itertools.combinations(last_level.nodes, n_level)
    candidates_merged = map(merge_nodes, candidates)
    next_level_nodes = list(filter(lambda n: len(n.attr_set) == n_level, candidates_merged))
    return next_level_nodes


def merge_nodes(nodes_list):
    return reduce(merge2node, nodes_list, FdNode([]))


def merge2node(node1, node2):
    node = FdNode([])
    node.attr_set = node1.attr_set | node2.attr_set
    return node






