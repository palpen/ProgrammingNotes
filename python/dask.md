# Notes on Dask

Some notes I'm taking while trying to learn Dask. Dask parallelizes Python code. It enables data analysis and machine learning for data that cannot fit in memory. It is great because it integrates well with the Python data ecosystem (numpy, pandas, scikit-learn).

## Basic Commands

### Loading list of csv files as a `dask.dataframe`
```
import dask.dataframe as dd

df = dd.read_csv('mydata_*.csv',
                 parse_dates={'Date': [0, 1, 2]})
```

### Exploring Data
* To see head: `df.head()`. To see head of say the third partition, `df.head(npartitions=3)`

## Setting up cluster for Dask
* This is from the scipy dask tutorial (referenced below). If a Kubernetes cluster is not available, the function sets up a local cluster

```
def make_cluster(**kwargs):
    try:
        from dask_kubernetes import KubeCluster
        kwargs.setdefault('n_workers', 9)
        cluster = KubeCluster(**kwargs)
    except ImportError:
        from distributed.deploy.local import LocalCluster
        cluster = LocalCluster()
    return cluster
```

## Random Notes

* Use `dask.delayed` for preprocessing that is specific to your dataset before loading it in as `dask.dataframe`
* Assuming `df` is a `dask.dataframe`, `df.compute()` returns the full pandas dataframe in memory. Be careful if dataset is very large!
* Speeding up computation by sharing intermediate results. Set up dask delays to compute mean and standard deviation:

    ```
    mean = df.SomeVar.mean()
    std = df.SomeVar.std()
    ```

    Now instead of running computation in sequence


    ```
    mean_res = mean.compute()
    std_res = std.compute()
    ```

    do

    ```
    mean_res, std_res = dask.compute(mean, std)
    ```

* How to use pandas methods that are not available in dask? Use `map_partitions`! Given that a `dask.dataframe` is just a collection of chunks of pandas dataframes, `map_partitions` can apply the pandas method to the individual pandas dataframes.

## Questions
* What does `persist()` do? How is it different from `compute()`?
    * `persist()` tells Dask to run the calculation but to persist the data in memory afterwards. It is useful for storing the intermediate result of an expensive operation. `compute()` does a quick calculation, but the calculation will have to be redone when running another downstream computation.
    * For example, setting the index on a large dataset can be expensive. Apply persis to save the result

    ```
    df = df.set_index("Date").persist()
    ```

    If we didn't apply persist

    ```
    df = df.set_index("Date")
    ```

    then every time we run `df.sum().compute()` dask will have to set the index since the reference of `df` is to `df.set_index("date")`

* What is a `dask.array`? How is it different from a `dask.dataframe`?
    * `dask.array` ...
    * `dask.dataframes` are parallelized pandas dataframes. The datasets are stored as individual pandas dataframes under the hood. The command `df.SomeVariable.max().visualize()` demonstrates this with a graph.
* What is `dask.delayed`? What does it

## Dask SciPy Tutorial, 2018
I found [this](https://www.youtube.com/watch?v=mqdglv9GnM8) Scipy tutorial on Dask in 2018 incredibly useful.  Here's the repo containing the notebooks for the tutorial:

* [Github Repo](https://github.com/martindurant/dask-tutorial-scipy-2018)

Here's a breakdown of the different notebooks and the corresponding timelines in the video:

1. [01-dask.delayed (4:31)](https://youtu.be/mqdglv9GnM8?t=271)
2. [02-dask-arrays (39:05)](https://youtu.be/mqdglv9GnM8?t=2344)
3. [03-dask-dataframes (1:18:15)](https://youtu.be/mqdglv9GnM8?t=4695)
4. [04-schedulers (1:48:37)](https://youtu.be/mqdglv9GnM8?t=6517)
5. [05-distributed-dataframes-and-efficiency (2:12:24)](https://youtu.be/mqdglv9GnM8?t=7936)
6. [06-distributed-advanced (2:38:26)](https://youtu.be/mqdglv9GnM8?t=9506)
7. [07-machine-learning (2:59:51)](https://youtu.be/mqdglv9GnM8?t=10791)


## References
1. [Scalable ML using Dask](https://www.youtube.com/watch?v=tQBovBvSDvA)
2. [Dask SciPy Tutorial (comprehensive)](https://www.youtube.com/watch?v=mqdglv9GnM8)
3. [Dask and XGBoost Experiment](https://www.youtube.com/watch?v=Cc4E-PdDSro)
