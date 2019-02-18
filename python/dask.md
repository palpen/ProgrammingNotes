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

## Questions
* What does `persist()` do?
* What is a `dask.array`? How is it different from a `dask.dataframe`?
    * `dask.array` ...
    * `dask.dataframes` are parallelized pandas dataframes. The datasets are stored as individual pandas dataframes under the hood. The command `df.SomeVariable.max().visualize()` demonstrates this with a graph.
* What is `dask.delayed`? What does it do?


## References
1. [Scalable ML using Dask](https://www.youtube.com/watch?v=tQBovBvSDvA)
2. [Dask SciPy Tutorial (comprehensive)](https://www.youtube.com/watch?v=mqdglv9GnM8)
3. [Dask and XGBoost Experiment](https://www.youtube.com/watch?v=Cc4E-PdDSro)
