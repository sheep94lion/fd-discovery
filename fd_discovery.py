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
            line_dict[i] = item
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
print is_fd([1], [3], data)