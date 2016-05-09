import itertools
from functools import reduce


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
    return reduce(merge2node, nodes_list, FdNode([]))


def merge2node(node1, node2):
    node = FdNode([])
    node.attr_set = node1.attr_set | node2.attr_set
    node.rhs_plus = node1.rhs_plus & node2.rhs_plus
    return node


def check_fd(x, y):
    return True


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

def compute_dependencies_one_level(l, alphabet):
    for node in l.nodes:
        candidates = node.rhs_plus & node.attr_set
        for e in candidates:
            if check_fd(node.attr_set - {e}, {e}):
                print(node.attr_set - {e}, e)
                node.rhs_plus.remove(e)
                node.rhs_plus = node.rhs_plus - (set(alphabet) - node.attr_set)
    l.nodes = list(filter(lambda n: n.rhs_plus != set(), l.nodes))
    return l


def compute_dependencies(alphabet):
    l = [Level(1, alphabet, 0)]
    for i in range(len(alphabet)):
        l[i] = compute_dependencies_one_level(l[i], alphabet)
        if i < len(alphabet) - 1:
            l.append(Level(i + 2, alphabet, l[i]))
