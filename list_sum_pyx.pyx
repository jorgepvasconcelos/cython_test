import array
from cpython cimport array

cpdef int list_sum(int range_list):
    cdef array.array generated_list = array.array('i', [*range(range_list)])

    cdef int a
    cdef int b
    cdef int last_number
    cdef array.array new_list = array.array('i', [])
    cdef bint first = True


    for value in generated_list:
        a = value

        if first:
            b = a
            first = False

        new_list.append(b + a)
        b = a

    return sum(new_list)
