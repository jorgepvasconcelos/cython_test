import cython


def list_sum(range_list: cython.uint) -> cython.uint:
    generated_list: cython.freelist = range(range_list)

    a: cython.uint
    b: cython.uint
    last_number: cython.int
    first: cython.bint = True

    new_list: cython.array = []

    for value in generated_list:
        a = value

        if first:
            b = a
            first = False

        new_list.append(b + a)
        b = a

    return sum(new_list)
