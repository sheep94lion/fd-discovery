import itertools
from functools import reduce
from fd_discovery import *


i = 0
results = []


class FdNode:
    def __init__(self, attr_list):
        self.attr_set = set(attr_list)
        self.rhs_plus = set([])


class Level:
    def __init__(self, n_level, alphabet, last_level):
        self.level = n_level
        if n_level == 1:
            self.nodes = []
            for c in alphabet:
                self.nodes.append(FdNode([c]))
            for node in self.nodes:
                node.rhs_plus = set(alphabet)
        else:
            self.nodes = generate_next_level(n_level, last_level)


def generate_next_level(n_level, last_level):
    candidates = itertools.combinations(last_level.nodes, n_level)
    candidates_merged = map(merge_nodes, candidates)
    next_level_nodes = list(filter(lambda n: len(n.attr_set) == n_level, candidates_merged))
    return next_level_nodes


def merge_nodes(nodes_list):
    return reduce(merge2node, nodes_list, nodes_list[0])


def merge2node(node1, node2):
    node = FdNode([])
    node.attr_set = node1.attr_set | node2.attr_set
    node.rhs_plus = node1.rhs_plus & node2.rhs_plus
    return node


def compute_dependencies_one_level(l, alphabet, data):
    global i
    global results
    for node in l.nodes:
        candidates = node.rhs_plus & node.attr_set
        for e in candidates:
            if is_fd(list(node.attr_set - {e}), list({e}), data):
                print(node.attr_set - {e}, e, i)
                item = (list(node.attr_set - {e}))
                item.extend([e])
                results.append(item)
                i += 1
                node.rhs_plus.remove(e)
                node.rhs_plus = node.rhs_plus - (set(alphabet) - node.attr_set)
    l.nodes = list(filter(lambda n: n.rhs_plus != set(), l.nodes))
    return l


def compute_dependencies(alphabet):
    data = read_file()
    l = [Level(1, alphabet, 0)]
    for i in range(len(alphabet)):
        if i > 0:
            l[i] = compute_dependencies_one_level(l[i], alphabet, data)
        if i < len(alphabet) - 1:
            l.append(Level(i + 2, alphabet, l[i]))


def output(r):
    file = open("result.txt", "w")
    for i in r:
        for a in range(len(i)):
            if a == len(i) - 1:
                file.write("-> ")
                file.write(str(i[a]))
                file.write("\n")
            else:
                file.write(str(i[a]))
                file.write(" ")


if __name__ == "__main__":
    global results
    compute_dependencies([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    r = sorted(results)
    output(r)

