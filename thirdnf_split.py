from bcnf_split import *
from fd_discovery import read_file


def get_candidate(alphabet, fd_dict):
    main_set = set(alphabet)
    flag = True
    candidate_list = alphabet.copy()
    while True:
        flag = True
        for item in candidate_list:
            temp_candidate_list = candidate_list.copy()
            temp_candidate_list.remove(item)
            if attributes_plus_compute(temp_candidate_list, fd_dict) == main_set:
                flag = False
                break
        
        if flag:
            break
        candidate_list = temp_candidate_list.copy()
    return set(candidate_list)


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


def get_canonical_cover(fd_dict, fd_list):
    while True:
        temp_dict = fd_dict.copy()
        for [key,item] in fd_list:
            if is_extraneous(key, item, fd_dict):
                break
        
        if temp_dict == fd_dict:
            break
    #print(fd_dict)
    return fd_dict


def third_nf_decomposition(alphabet, fd_dict, fd_list):
    result = []
    flag = True
    canonical = get_canonical_cover(fd_dict, fd_list)
    i = 0
    for key, item in canonical.items():
        flag = True
        relation_set = set(eval(key) + item)
        for k in range(1, i+1):
            if relation_set.issubset(result[k-1]):
                flag = False
                break
        if flag:
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
    return result


def generate_input():
    (fd_dict, fd_list) = read_result_file()
    result_set = third_nf_decomposition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], fd_dict, fd_list)
    result_list = [list(x) for x in result_set]
    print(result_list)
    return result_list

if __name__ == '__main__':
    generate_input()
