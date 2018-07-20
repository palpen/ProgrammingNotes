# Notes, templates, and techniques on the Python programming language


## Template for argparse


## Basic template for functions decorators
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

## How to create n equal sized chunks from a list
```python
def make_chunks(num_chunks):
    chunks = []
    for i in range(num_chunks):
        file_chunks = proc_files[i::num_chunks]
        chunks.append(file_chunks)
    return chunks
```