# Notes on Dask

## Basic Commands

### Loading list of csv files as a `dask.dataframe`
```
import dask.dataframe as dd

df = dd.read_csv('mydata_*.csv',
                 parse_dates={'Date': [0, 1, 2]})
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
* What does `persist()` do?
* What is a `dask.array`? How is it different from a `dask.dataframe`?
    * `dask.array` ...
    * `dask.dataframes` are parallelized pandas dataframes. The datasets are stored as individual pandas dataframes under the hood. The command `df.SomeVariable.max().visualize()` demonstrates this with a graph.
* What is `dask.delayed`? What does it


## References
1. [Scalable ML using Dask](https://www.youtube.com/watch?v=tQBovBvSDvA)
2. [Dask SciPy Tutorial (comprehensive)](https://www.youtube.com/watch?v=mqdglv9GnM8)
3. [Dask and XGBoost Experiment](https://www.youtube.com/watch?v=Cc4E-PdDSro)
