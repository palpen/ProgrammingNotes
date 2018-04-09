# Data Analysis Tricks

## Given a dictionary of columns and their corresponding labels, create a nicely formatted summary statistic table
```python
cols_labels = {'price_p1_var': 'Mean Avg. Variable Price - Period 1', 
                     'price_p2_var': 'Mean Avg. Variable Price - Period 2',
                     'price_p3_var': 'Mean Avg. Variable Price - Period 3', 
                     'price_p1_fix': 'Mean Avg. Fixed Price - Period 1',
                     'price_p2_fix': 'Mean Avg. Fixed Price - Period 2', 
                     'price_p3_fix': 'Mean Avg. Fixed Price - Period 3'}
cols = [c for c in cols_labels.keys()]  # get column names
price_desc = df[cols].describe().round(3).T  # create sum. stat. table
price_desc.rename(index=cols_labels)  # replace column names with labels
```
