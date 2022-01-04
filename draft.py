from random import randint


def generate_list_rand_int():
    result = [randint(1, 10) for _ in range(20)]
    return result


def print_str(some_string):
    print(some_string)


def print_reverse_str(some_string):
    print(some_string[::-1])


def get_reverse_str(some_string):
    return some_string[::-1]


def change_list_last_value(my_list, last_value):
    # if not my_list:
    #     return my_list
    my_list.pop()
    my_list.append(last_value)
    return my_list
