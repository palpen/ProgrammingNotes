# How to parallelize code in Python

### References
* [Concurrent.futures vs multiprocessing in Python 3](https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3)
* [What do the terms CPU bound and IO bound mean?](https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)
* [Why is a Python IO bound task not blocked by the GIL](https://stackoverflow.com/questions/29270818/why-is-a-python-i-o-bound-task-not-blocked-by-the-gil)

The code below shows

- Multithreading using the `ThreadPoolExecutor` class from the `concurrent.futures` library
- Display progress meter using the `tqdm` library

The first approach--using functions `f` and `run`--executes the task and consumes the results only after __all__ the threads are finished processing their inputs

The second approach--using functions `f_consume_now` and `run_consume_now`--executes the task and consumes the results as they are completed (by appending them to a list)

The second approach is useful in cases where a long-running process may be interrupted. In such case, one could capture the exception and export the data saved before the interruption.

This video explains the module really well:
* EuroPython 2012, Andrew Dalke: https://www.youtube.com/watch?v=2Ng-UIedZMY

Other useful references:
* https://docs.python-guide.org/scenarios/speed/
* https://docs.python.org/3/library/concurrent.futures.html

```python
import time
import concurrent.futures
from tqdm import tqdm


def f(x):
    time.sleep(0.001)  # to visualize the progress
    return x**2


def run(f, my_iter):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = tqdm(
                    executor.map(f, my_iter),
                    total=len(my_iter)
                    )
        final_results = list(results)
    return final_results


def f_consume_now(file, client):
    time.sleep(0.01)
    return "Processed " + file, client


def run_consume_now(f, args, number_workers=10):

    final_results = []

    with concurrent.futures.ThreadPoolExecutor(number_workers) as executor:

        results = {
            executor.submit(lambda p: f(*p), item): a for a in args
            }

        completed_results = concurrent.futures.as_completed(results)

        for future in tqdm(completed_results, total=len(args)):
            processed_file, client = future.result()
            final_results.append((processed_file, client))

    return final_results


if __name__ == '__main__':

    # Consume only after all threads are finished
    # my_iter = range(100000)
    # run(f, my_iter)

    # Consume as each input is processed
    file_list = [f"file {x}" for x in range(10000)]
    args = [(call, "gcp client service") for call in file_list]
    final_results = run_consume_now(
        f_consume_now,
        args,
        number_workers=1000
    )

    print(
        f"Len final results: {len(final_results)}",
        f"Preview final results: {final_results[0:5]}",
        sep='\n'
    )
```
