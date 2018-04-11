# Notes, templates, and techniques on the Python programming language

## Basic template for functions decorators
```python
def my_decorator(my_function):
    def wrapper():
        print("Test before function call")
        my_function()
        print("Test after function call")
    return wrapper

def my_function():
    print("This is my_function!")

just_some_function = my_decorator(just_some_function)
just_some_function()

# Using decorator syntactic sugar
@my_decorator
def my_function():
    print("This is my_function!")

just_some_function()
```