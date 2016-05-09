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


def read_file():
    file = open("data.txt")
    data = []
    while 1:
        line = file.readline()
        if not line:
            break

        line_list = line[0:-1].split(',')
        line_dict = {}
        i = 1
        for item in line_list:
            line_dict[str(i)] = item
            i += 1
        data.append(line_dict)
    return data


def get_partition(data, list):
    partition = {}
    i = 1
    for item_data in data:
        attr = ''
        for item_list in list:
            attr += item_data[item_list]
        if attr in partition:
            partition[attr].append(i)
        else:
            partition[attr] = [i]
        i += 1

    return partition


def is_fd(list1, list2, data):
    l1 = len(get_partition(data, list1).keys())
    list_union = list(set(list1).union(set(list2)))
    l2 = len(get_partition(data, list_union).keys())
    if l1 == l2:
        return True
    else:
        return False


data = read_file()
print data[1]
print len(data)
print is_fd(['1', '2'], ['4', '5'], data)



