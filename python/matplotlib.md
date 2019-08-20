## How to place plots in figs and axes

Put multiple figures in same fig and axis

```python
fig, ax = plt.subplots(figsize=(10, 5))
df.plot('x_var', 'y_var_1', ax=ax)
df.plot('x_var', 'y_var_2', ax=ax)
plt.show()
```

Multiple plots in same figure but in separate axis

```python
num_row = 1
num_col = 2
fig, (ax1, ax2) = plt.subplots(num_row, num_col, figsize=(13, 5))
df.plot('x_var', 'y_var_1', ax=ax1)
df.plot('x_var', 'y_var_2', ax=ax2)
plt.show()
```

It's also possible to generate the plots directly from the axis objects, which is useful because it doesn't require data to be stored in Pandas

```python
fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(df['x_var'], df['y_var'])
plt.show()
```

## Saving figure

After generating the image, invoke

```python
plt.savefig('myfig.pdf', bbox_inches='tight', dpi=300)
```

`bbox_inches='tight'` removes the figure's margins


## How to show an image
```python
import matplotlib.pyplot as plt
img = plt.imread('my_image.jpg')
plt.imshow(img);
plt.show();
```

## Setting interactive backend
```python
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
```

# Various useful features

#### Fix regular interval along x axis
May not get expected result for datetime objects
```
loc = ticker.MultipleLocator(base=4.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)
```
[source](https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib)
