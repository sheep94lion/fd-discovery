from bcnf_split import *


def get_candidate(alphabet, fd_dict):
    main_set = set(alphabet)
    candidate_list = alphabet.copy()
    while True:
        temp_candidate_list = candidate_list.copy()
        temp_candidate_list.pop()
        if attributes_plus_compute(temp_candidate_list, fd_dict) != main_set:
            return set(candidate_list)
        candidate_list = temp_candidate_list.copy()


def is_extraneous(left_list, right_list, fd_dict):
    for item in left_list:
        temp_list = left_list.copy()
        temp_list.remove(item)
        temp_result = attributes_plus_compute(temp_list, fd_dict)
        if set(right_list).issubset(temp_result):
            fd_dict.pop(str(left_list))
            fd_dict[str(temp_list)] = right_list
            return True

    temp_dict = fd_dict.copy()
    for item in right_list:
        temp_list = right_list.copy()
        temp_list.remove(item)
        temp_dict[str(left_list)] = temp_list
        temp_result = attributes_plus_compute(left_list, temp_dict)
        if item in temp_result:
            fd_dict[str(left_list)] = temp_list
            return True

    return False


def get_canonical_cover(fd_dict):
    while True:
        temp_dict = fd_dict.copy()
        for key,item in temp_dict.items():
            if is_extraneous(eval(key), item, fd_dict):
                break
        if temp_dict == fd_dict:
            break
    #print(fd_dict)
    return fd_dict


def third_nf_decomposition(alphabet, fd_dict):
    result = []
    flag = True
    canonical = get_canonical_cover(fd_dict)
    i = 0
    for key, item in canonical.items():
        relation_set = set(eval(key) + item)
        for k in range(1, i+1):
            if relation_set.issubset(result[k-1]):
                flag = False
                break
        if flag:
            flag = True
            i += 1
            result.append(relation_set)

    flag = True
    for item in result:
        right_list = attributes_plus_compute(list(item), fd_dict)
        if set(right_list) == set(alphabet):
            flag = False
            break
    if flag:
        result.append(get_candidate(alphabet, fd_dict))

    flag = True
    while True:
        temp_result = result.copy()
        for item in result:
            for temp_item in temp_result:
                if item != temp_item and temp_item.issubset(item):
                    flag = False
                    temp_result.remove(temp_item)
                    break
            if not flag:
                flag = True
                break
        if result == temp_result:
            break
        result = temp_result.copy()
    print(result)
    return result


def generate_input():
    fd_dict = read_file()
    result_set = third_nf_decomposition([1,2,3,4,5,6,7,8,9,10,11,12], fd_dict)
    result_list = [list(x) for x in result_set]
    print(result_list)
    return result_list

if __name__ == '__main__':
    generate_input()
    #fd_dict = read_file()
    #third_nf_decomposition([1,2,3,4,5,6,7,8,9,10,11,12], fd_dict)