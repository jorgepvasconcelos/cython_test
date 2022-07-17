import cython


def list_sum(range_list: cython.uint) -> cython.uint:
    generated_list: cython.freelist = range(range_list)

    a: cython.uint
    b: cython.uint
    last_number: cython.int

    len_list: cython.uint = len(generated_list)
    new_list: cython.array = []

    for index, value in enumerate(generated_list):
        a = value
        if index == len_list:
            b = last_number
        else:
            b = generated_list[index]
            last_number = b

        new_list.append(b + a)

    return sum(new_list)
