# Notes on Pandas

## Code Snippets

1. Loop through each column and convert object to integer
```python
cols = list(df.columns.values)
for c in cols:
    try:
        df[c] = df[c].astype(str).astype(int)
    except Exception as e:
        print("Cannot cast to int:", e)
```

2. Create arbitrary dataframe with random values

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 3), columns=['a', 'b', 'c'])
```

3. Quickly plot and save figure

```python
import pandas as pd; df = pd.read_csv('mydata.csv')
ax = df.plot('x_col', figsize=(14, 9))  # x_col is column in x-axis; figsize=(width, height)
fig = ax.get_figure()
fig.savefig('myplot.png')
```

## Settings

* Increase number of rows to display: `pd.set_option('display.max_rows', 1000)`
