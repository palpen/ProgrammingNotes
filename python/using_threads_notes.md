# An Example using the Threading Module

## When is this useful

You need to make an api call over a long list of files and would like to parallelize the procedure in order to finish it more quickly.

## Basic outline

In addition to whatever library you need to make your API call, you need the `threading` module to implement the steps below. This is part of Pyton's standard library so there's no need to install anything. You'll also need `json` (also part of the standard library) if you want to save the results of you calls.

1. Split the list of files into some n number of chunks. The number of chunks depend on the limit of the service you are using. If, for example, the service limit is 10 calls per second, then split your list of files into 10 chunks. The function to create chunks from a list is as follows:

```python
def make_chunks(l: List[str], num_chunks: int):
    chunks = []
    for i in range(num_chunks):
        file_chunks = l[i::num_chunks]
        chunks.append(file_chunks)
    return chunks
```

2. Create function that would make an api call to each file in a given chunk in a sequential way. This function should save result to some data structure, such as a dictionary.

```python
def chunk_processor(chunk: List[str], store: Dict=None):
    if store is None:
        store = {}
    for file in chunk:
        result = api_call(file)
        store[file] = result
    return store
```

The `api_call` function is some function that makes an API call on `file`. `file` could be a file containing spoken text and `api_call` makes an API call to some service that calculates the sentiment score of the spoken text in `file`. Once the function is finished iterating through each file in `chunk`, we return the dictionary, `store`.

3. Threading happends in the script below
```python
store = {}
threads = []

for file_list in files_chunks:
    t = Thread(target=chunk_processor, args=(file_list, store))
    threads.append(t)

[t.start() for t in threads]  # start threads
[t.join() for t in threads]  # wait for threads to finish

print("All threads have finished!")
```

The loop above creates an instance of the Thread class given the `chunk_processor` function defined in 2. and a chunk from `files_chunk` (created by the `make_chunks` function in 1.).
The threads are started (the actual parallelized API calls) in the list comprehension directly below.

The list comprehension `[t.join() for t in threads]` waits until the main thread is finished before proceeding. In other words, we want all threads to finish iterating through their chunk before the final line that prints "All threads have finished!" is executed.

The threads will save all the results of their calls to the `store` dictionary. Save this to a json file with the code below:

```python
# export as json
with open('api_call_results.json', 'w') as fp:
    json.dump(store, fp)
```

## Putting it all together

```python
from threading import Thread


def make_chunks(l: List[str], num_chunks: int):
    chunks = []
    for i in range(num_chunks):
        file_chunks = l[i::num_chunks]
        chunks.append(file_chunks)
    return chunks


def chunk_processor(chunk: List[str], store: Dict=None):
    if store is None:
        store = {}
    for file in chunk:
        result = api_call(file)
        store[file] = result
    return store


if __name__ == '__main__':

    files = [
        'file1.txt', 'file2.txt', 'file3.txt',
        'file4.txt', 'file5.txt', 'file6.txt',
        'file7.txt', 'file8.txt', 'file9.txt',
    ]

    file_chunks = make_chunks(files, 3)

    store = {}
    threads = []

    for file_list in files_chunks:
        t = Thread(target=chunk_processor, args=(file_list, store))
        threads.append(t)

    [t.start() for t in threads]  # start threads
    [t.join() for t in threads]  # wait for threads to finish

    print("All threads have finished!")

    # export as json
    with open('api_call_results.json', 'w') as fp:
        json.dump(store, fp)

```

## Resources
1. https://en.wikibooks.org/wiki/Python_Programming/Threading
2. https://stackoverflow.com/questions/16982569/making-multiple-api-calls-in-parallel-using-python-ipython
