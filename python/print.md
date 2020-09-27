
## Aligning  in a print statement

```python
for r in [('a', 123123, 34234), ('aaaaaaa', '2', '1231234234')]:
    print('{0:=<25}{1:_<25}{2:+<20}'.format(r[0], r[1], r[2]))
```
