from myapproach import get_cleaned_string, get_cleaned_data
import pytest


@pytest.fixture
def my_funcs():
    def strip_(x):
        return x.strip()

    def upper_(x):
        return x.upper()

    def lower_(x):
        return x.lower()

    funcs1 = [strip_, upper_]
    funcs2 = [strip_, lower_]

    return funcs1, funcs2


@pytest.fixture
def my_data():
    return ['This is a book.', 'That is an apple.']


@pytest.mark.parametrize('not_string',
                         [(1),
                          ([1, 2, 3]),
                          ((1, 2, 3)),
                          ({1, 2, 3}),
                          ({'a': 1, 'b': 2, 'c': 3}),
                          ])
def test_not_string(not_string, my_funcs):
    with pytest.raises(TypeError):
        get_cleaned_string(not_string, my_funcs)


@ pytest.mark.parametrize('my_string',
                          [('This is a book.'),
                           ('THIS IS a book.'),
                           (' This is a book.'),
                           ('This is a book. '),
                           (' This is a book. '),
                           ('   This is a book.  '),
                           ])
def test_get_cleaned_string(my_funcs, my_string):
    funcs1, funcs2 = my_funcs
    assert get_cleaned_string(my_string, funcs1) == 'THIS IS A BOOK.'
    assert get_cleaned_string(my_string, funcs2) == 'this is a book.'


def test_get_cleaned_data(my_funcs, my_data):
    funcs1, funcs2 = my_funcs
    output1 = get_cleaned_data(my_data, funcs1)
    output2 = get_cleaned_data(my_data, funcs2)

    assert len(output1) == len(output2) == len(my_data)
    assert type(output1) == type(output2) == type(my_data)
    assert output1 == ['THIS IS A BOOK.', 'THAT IS AN APPLE.']
    assert output2 == ['this is a book.', 'that is an apple.']
