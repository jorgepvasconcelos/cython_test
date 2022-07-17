def list_sum(range_list: int):
    generated_list = range(range_list)

    a: int = 0
    b: int = 0
    first: bool = True

    new_list: list = []
    last_number: int

    for value in generated_list:
        a = value

        if first:
            b = a
            first = False

        new_list.append(b + a)
        b = a

    return sum(new_list)
