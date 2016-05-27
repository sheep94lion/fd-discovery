list_len = 0
def read_result_file():
    global list_len
    file = open("result.txt")
    fd_dict = dict()
    while 1:
        line = file.readline()
        if not line:
            break
        list_len += 1
        if line[-1] == '\n':
            line = line[0:-1]
        line_list = line.split(' ')
        fd = []
        for item in line_list:
            if item != "->":
                fd.append(int(item))
        key = str(fd[0:-1])
        if key not in fd_dict:
            fd_dict[key] = [fd[-1]]
        else:
            fd_dict[key].append(fd[-1])
    #print(fd_dict['[1]'])
    #print(fd_dict)
    print(len(fd_dict))
    return fd_dict


def get_all_subsets(alphabet):
    attributes_list = [[]]
    for item in alphabet:
        temp_attributes = []
        for item_attribute in attributes_list:
            temp = item_attribute.copy()
            item_attribute.append(item) 
            temp_attributes.append(item_attribute)
            temp_attributes.append(temp)
        attributes_list = temp_attributes
    attributes_list = sorted(attributes_list)
    return attributes_list


def attributes_plus_compute(attr_list, fd_dict):
    result = set(attr_list)
    while True:
        temp_result = result.copy()
        for key, item in fd_dict.items():
            if set(eval(key)).issubset(result):
                for attr_item in item:
                    temp_result.add(attr_item)
        if temp_result == result:
            break
        result = temp_result.copy()
    #print(result)
    return result


def bcnf_decomposition(alphabet, fd_dict):
    result = [set(alphabet)]
    flag = True
    while True:
        temp_result = result.copy()
        for key, item in fd_dict.items():
            for set_item in result:
                set_key = set(eval(key))
                if set_key.issubset(set_item):
                    key_plus = set_item - attributes_plus_compute(eval(key), fd_dict)
                    if key_plus != set() and key_plus != set_item - set_key:
                        temp_result.remove(set_item)
                        temp_result.append(key_plus | set_key)
                        temp_result.append(set_item - key_plus)
                        flag = False
                        break
            if not flag:
                flag = True
                break

        if temp_result == result:
            break
        result = temp_result.copy()
    print(result)
    return result


def bcnf_generate_input():
    fd_dict = read_result_file()
    for i in fd_dict:
        print(i)
    result_set = bcnf_decomposition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], fd_dict)
    result_list = [list(x) for x in result_set]
    return result_list



