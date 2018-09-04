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

4. How to set up logging using the `logging` module
Near the top of your script, add
```python
import logging
logging.basicConfig(filename="mylogfile.log", level=logging.DEBUG)

# Rest of script goes here
```
Notes on logging:
1. https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
2. https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

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

2. How to load and append a collection of json files into one dataframe
```python
import pandas as pd
import json

appended_data = []
files = p.glob("myfiles_*.json")

for infile in files:

    with open(infile, 'r') as f:
        json_data = json.load(f)

    df_data = pd.DataFrame(json_data)
    df_data = df_data.T.sort_index()
    appended_data.append(df_data)

df = pd.concat(appended_data, axis=0)
```

3. Understanding the `sorted` function and how it sorts dictionary keys by value

`sorted` returns a new sorted list from the items in iterable.

Any iterable is acceptable (e.g. sequences such as strings or lists or collections such as sets or dictionaries)

If you try to sort a dictionary, it will sort by its keys and return a list containing the sorted keys

```
>>>> sample_dict = {0: 'b', 1: 'a', 2: 'c'}
>>> sorted(sample_dict)
>>> [0, 1, 2]
```

By default, passing a dictionary into `sorted` will always return the keys.

If you want to sort by the values of the dictionary, you need to pass a function to the key argument in `sorted` the input of which will be the items in the iterable (if its a dictionary, then the input to this function will be its keys):

```
>>> sorted(sample_dict, key=sample_dict.get)
>>> [1, 0, 2]
```

In this case, the input to `sample_dict.get()` are the keys of sample_dict. `sample_dict.get()` returns the value given a key. This, in effect, will sort the output of `sorted` by sample_dict's values but return the keys

If you want to sort by values and return the sorted values themselves, do

```
>>> sorted(sample_dict.values())
>>> ['a', 'b', 'c']
```


