class FdNode:
    def __init__(self, attr_list):
        self.attr_set = set(attr_list)


class Level:
    def __init__(self, n_level, alphabet, last_level):
        if n_level == 1:
            for c in alphabet:
                self.nodes = []
                self.nodes.append(FdNode([c]))
        else:
            self = generate_next_level(n_level, last_level)
    def generate_next_level(self, n_level, last_level):


if __name__ == "__main__":
    print(1)




