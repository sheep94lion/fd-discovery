partition_list = {}
list_len = 0


def read_file():
    global list_len
    file = open("data.txt")
    data = []
    while 1:
        line = file.readline()
        if not line:
            break
        list_len += 1
        if line[-1] == '\n':
            line = line[0:-1]
        line_list = line.split(',')
        line_dict = {}
        i = 1
        for item in line_list:
            line_dict[i] = item
            i += 1
        data.append(line_dict)
    return data


def get_partition(data, list):
    partition = {}
    len = 0
    i = 1
    for item_data in data:
        attr = ''
        for item_list in list:
            attr += item_data[item_list]
            attr += '+'
        if attr in partition:
            partition[attr].append(i)
        else:
            partition[attr] = [i]
            len += 1
        i += 1

    return len


def get_partnum(list, data):
    global partition_list
    attr = str(sorted(list))
    if attr in partition_list:
        l = partition_list[attr]
    else:
        l = get_partition(data, list)
        partition_list[attr] = l

    return l


def is_fd(list1, list2, data):
    global list_len
    l1 = get_partnum(list1, data)
    if l1 == list_len:
        return True
    list_union = list(set(list1).union(set(list2)))
    l2 = get_partnum(list_union, data)

    if l1 == l2:
        return True
    else:
        return False