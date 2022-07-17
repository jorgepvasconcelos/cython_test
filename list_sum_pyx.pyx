import array
from cpython cimport array

cpdef int list_sum(int range_list):
    cdef array.array generated_list = array.array('i', [*range(range_list)])

    cdef int a
    cdef int b
    cdef int last_number
    cdef int len_list
    cdef array.array new_list

    len_list = len(generated_list)
    new_list = array.array('i', [])

    for index, value in enumerate(generated_list):
        a = value
        if index == len_list:
            b = last_number
        else:
            b = generated_list[index]
            last_number = b

        new_list.append(b + a)

    return sum(new_list)
