import array
from cpython cimport array

cpdef unsigned long long int list_sum(unsigned long long int range_list):
    cdef array.array generated_list = array.array('i', [*range(range_list)])

    cdef unsigned long long int a = 0
    cdef unsigned long long int b = 0
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
