import cython


def list_sum(range_list: cython.int):
    generated_list = range(range_list)

    a: cython.int
    b: cython.int
    len_list = len(generated_list)

    new_list: list = []
    last_number: cython.int

    for index, value in enumerate(generated_list):
        a = value
        if index == len_list:
            b = last_number
        else:
            b = generated_list[index]
            last_number = b

        new_list.append(b + a)

    return sum(new_list)
