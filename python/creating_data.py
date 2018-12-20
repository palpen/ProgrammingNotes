'''
Quickly create play data in pandas for testing

Just copy and paste the desired data set in your REPL
to quickly generate the data you want to play with

For a richer set of play data, see pandas.util.testing
e.g.
import pandas.util.testing as tm
df = tm.makeTimeDataFrame(freq='M').head()
df = tm.makeMissingDataframe()
'''

import pandas as pd
import numpy as np

# Manually entered data
data = {
    'c1': [1, 2, 3, 4],
    'c2': [5, 6, 7, 8],
    'c3': ['a', 'b', 'c']
}
df = pd.DataFrame(data)

# Random integers
data = np.random.randint(low=0, high=10, size=(15, 5))
df = pd.DataFrame(data)

# Random floats
data = np.random.random_sample(size=(15, 5))
df = pd.DataFrame(data)

# Random floats with columns
data = np.random.random_sample(size=(15, 5))
df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e'])

# Random strings
def random_hexstr():
    '''Hex string'''
    return f"{random.randrange(3**30): 02X}".strip()

data = [random_hexstr() for _ in range(15)]
df = pd.DataFrame(data)

# Date data (dtype = datetime64[ns])
df = pd.DataFrame(pd.date_range(start='1/1/2018', periods=30))

# Date data with start and end date and arbitrary period
dates_data = pd.date_range(start='2018-04-24', end='2018-04-27', periods=400)
df = pd.DataFrame(dates_data)

# Date data as string
df = pd.DataFrame(pd.date_range(start='1/1/2018', periods=30).astype(str))

# Random missing rows
# Note: Numpy nan are for float arrays only
data = np.random.random_sample(size=(15, 5))
data[data > 0.3] = np.nan
df = pd.DataFrame(data)

# Random missing strings
def random_hexstr():
    '''Hex string'''
    return f"{random.randrange(3**30): 02X}".strip()

data = [random_hexstr() for _ in range(15)]
df = pd.DataFrame(data)
df.iloc[df.sample(frac=0.3).index, 0] = np.nan

# Ints, floats, strings, missing floatas, and dates
nrows = 15  # Number of rows
ints_data  = np.random.randint(low=0, high=10, size=(nrows, 1)).flatten()
floats_data = np.random.random_sample(size=(nrows, 1)).flatten()
strings_data = [random_hexstr() for _ in range(nrows)]
dates = pd.date_range(start='1/1/2018', periods=nrows)
floats_nan_data = np.random.random_sample(size=(nrows, 1))
floats_nan_data[floats_nan_data > 0.3] = np.nan
floats_nan_data = floats_nan_data.flatten()

data = {
    "ints": ints_data,
    "floats": floats_data,
    "strings": strings_data,
    "floats_missing": floats_nan_data,
    "dates": dates
}
df = pd.DataFrame(data)

