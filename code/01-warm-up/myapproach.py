def get_cleaned_string(x, funcs):
    for func in funcs:
        x = func(x)
    return x


def get_cleaned_data(data, funcs):
    return [get_cleaned_string(one_data, funcs) for one_data in data]


if __name__ == '__main__':
    my_input = [' This is a book. ', '  tHAT iS aN aPPLE.  ']
    funcs = [lambda x: x.strip(), lambda x: x.upper()]
    my_output = get_cleaned_data(my_input, funcs)
    print(my_output)
