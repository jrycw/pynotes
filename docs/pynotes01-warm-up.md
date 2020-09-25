# pynotes01-warm-up

[TOC]

## Origin
How to apply a series of predefined functions to a given iterable and then return the result whose type is the same as given?

## Exercise
### Input
```python
my_input = [' This is a book. ', '  tHAT iS aN aPPLE.  ']
```
### Desired output
```python
my_output = ['THIS IS A BOOK.', 'THAT IS AN APPLE']
```

### Challenges
1. Handle the empty space both appears in the beginning and the end of `my_input`
2. Turn each word in `my_input` to uppercase
3. Get a list back(the type of `my_input` is `list`)


## Hands-on
### Approach01
``` python
if __name__ == '__main__':
    my_input = [' This is a book. ', '  tHAT iS aN aPPLE.  ']
    my_output = [i.strip().upper() for i in my_input]
```
Fantastic! We need just one line of code to resolve the exercise.
Well, the code does resolve the problem, but it also incurs some potential issues. 

??? warning "Issue"
    === "Issue01-a"
        What if we have multiple operations needed to apply to `my_input`. This means that we need to change the code to chain more operations to `i.strip().upper()`. What's worse, what if we need a custom operation that `str` does not support.

    === "Issue01-b"
        What if we only want to get the result of part of `my_input`.For instance,the result of `my_input[0]`. Again, we need to change the code.

### Approach02
``` python hl_lines="4 5"
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
```
This approach looks more structured. Let's check what improvements we have made.

* We create a `funcs` list to collect the operations we would like to apply for `my_input`. Note that I use the `lambda` expression here, since our operation is relatively easy and will be used once, but you can, of course, define a function to handle the more complex operation. 
* We define a `get_cleaned_data` function, which includes the core implementation for this exercise. That's great, because we can use the function again and again without modifying it (if it is well-planned).

!!! Tip 
    === "Name iterables as plural"
        It is almost always a good habit to name your iterables as plural, so that instead of thinking about what name should be used while iterating,  you can just simply use the single of iterables. I reckon this is more pythonic.  

    === "Powerful for-loop pattern"
        Please note that the main point of `get_cleaned_data` relies on `line4` & `line5`. These 2 lines allow us to apply our custom functions sequentially to `x`. You should definitely save this technique to your arsenal.

Without modifying our core implementation,`get_cleaned_data`, we now can

* Easily inject the custom operations into`funcs`.
* Slice `my_input` to the shape we want, and then throw in `get_cleaned_data` as a parameter.

`Issue01-a` & `Issue01-b` are resolved. Everything seems perfect! What else can we do?

??? warning "Issue"
    === "Issue02"
        `get_cleaned_data` function not only performs operations to each element of `my_data`, but also collects the results. Actually, it has too many responsibilities. In Python, we prefer constructing many small functions instead of one giant function. Each function should do only one thing but do it perfectly.

### MyApproach
``` python
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
```
We create a `get_cleaned_string` function and ask it to handle the operation for one element of `my_input` only. Then we rewrite `get_cleaned_data` to collect the results after performing `get_cleaned_string` via the list comprehension. `Issue02` is resolved.

The structure looks more elegant, doesn't it? This kind of pattern is often used in `class` when you need to define the methods.

## Summary

!!! success "In `pynotes01`, we learned:"
    1. `funcs` helps us create the pipeline for the operations.
    2. `lambda` function is sometimes  handy to use.
    3. Using one for-loop, you can easily apply `funcs` to one element of `my_input`.
    4. The concept of separation `get_cleaned_string` and `get_cleaned_data` is crucial to be recognized.


