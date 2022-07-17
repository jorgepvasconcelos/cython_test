from timeit import timeit

py = timeit(stmt='list_sum(10000)', number=100, setup='from list_sum_py import list_sum')
# cy = timeit(stmt='list_sum(100000)', number=100, setup='from list_sum_cy import list_sum')
px = timeit('list_sum(10000)', number=100, setup='from list_sum_pyx import list_sum')
# cc = timeit('list_sum(100000000)', number=10, setup='from list_sum_py import list_sum')

print('Python Puro', py)
# print('Python com tipos em Cython', cy)
print('Cython Puro', px)
# print('C Puro', cc)

# print(f'{py/cy=}')
print(f'{py/px=}')
# print(f'{py/cc=}')
# print(f'{cy/cc=}')
# print(f'{px/cc=}')
