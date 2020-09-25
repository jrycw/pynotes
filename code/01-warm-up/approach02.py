def get_cleaned_data(data, funcs):
    my_output = []
    for x in data:
        for func in funcs:
            x = func(x)
        my_output.append(x)
    return my_output


if __name__ == '__main__':
    my_input = [' This is a book. ', '  tHAT iS aN aPPLE.  ']
    funcs = [lambda x: x.strip(), lambda x: x.upper()]
    my_output = get_cleaned_data(my_input, funcs)
    print(my_output)
