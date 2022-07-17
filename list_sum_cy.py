import cython


def list_sum(range_list: cython.ulonglongint) -> cython.ulonglongint:
    generated_list: cython.freelist = range(range_list)

    a: cython.ulonglongint = 0
    b: cython.ulonglongint = 0
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
