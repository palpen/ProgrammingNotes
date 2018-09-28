# Threading using ThreadPoolExecutor from concurrent.futures

The code below shows

- Multithreading using the `ThreadPoolExecutor` class from the `concurrent.futures` library
- Display progress meter using the `tqdm` library

The first approach--using functions `f` and `run`--executes the task and consumes the results only after __all__ the threads are finished processing their inputs

The second approach--using functions `f_consume_now` and `run_consume_now`--executes the task and consumes the results as they are completed (by appending them to a list)

Second approach is useful in cases where there is concern that a long-running process will be interrupted. In such case, one could capture the exception and export the data saved before the exception was raised.

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


def run_consume_now(f, my_iter, number_workers=10):

    final_results = []

    with concurrent.futures.ThreadPoolExecutor(number_workers) as executor:

        results = {
            executor.submit(lambda p: f(*p), item): item for item in my_iter
            }

        completed_results = concurrent.futures.as_completed(results)

        for future in tqdm(completed_results, total=len(my_iter)):
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
    final_results = run_consume_now(f_consume_now,
                                    args,
                                    number_workers=1)

    print(f"Len final results: {len(final_results)}",
          f"Preview final results: {final_results[0:5]}",
          sep='\n')
```
