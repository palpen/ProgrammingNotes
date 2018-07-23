# Pandas Code Snippets

1. Loop through each column and convert object to integer
```python
cols = list(df.columns.values)
for c in cols:
    try:
        df[c] = df[c].astype(str).astype(int)
    except Exception as e:
        print("Cannot cast to int:", e)
```