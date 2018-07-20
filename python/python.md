# Notes, templates, and techniques for Python

## Templates 

1. Creating function decorators
```python
def my_decorator(my_function):
    def wrapper(x):
        print("Test before function call")
        my_function(x)
        print("Test after function call")
    return wrapper


def my_function(x):
    print("This is my_function with arguement {}".format(x))


my_function = my_decorator(my_function)
my_function("arg")

# Using decorator syntactic sugar
@my_decorator
def my_function():
    print("This is my_function!")

my_function("arg")
```

2. Template for argparse
???

3. Template for pytest
???

## Misc. Techniques
1. How to create n equal-sized subsets of a list
```python
def make_chunks(l, num_chunks):``
    chunks = []
    for i in range(num_chunks):
        file_chunks = l[i::num_chunks]
        chunks.append(file_chunks)
    return chunks
```

