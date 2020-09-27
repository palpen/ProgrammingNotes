
## Aligning  in a print statement

To align the output of columnar data, use the format string syntax

```python
for r in [('a', 123123, 34234), ('aaaaaaa', '2', '1231234234')]:
    print('{0:=<25}{1:_<25}{2:+<20}'.format(r[0], r[1], r[2]))
```
This should produce the output

```
a========================123123___________________34234+++++++++++++++
aaaaaaa==================2________________________1231234234++++++++++
```

`{0:=<25}` says to indent the content of the first item, `r[0]`, to the left, give it 25 characters of space and fill any white space with the character `=`.

The `=`, `_`, and `+` characters in the string makes it easy to visualize and debug the alignment. Removing them will give you the desired output

```
a                        123123                   34234
aaaaaaa                  2                        1231234234
```

See this page for a description of the various alignment options:

https://docs.python.org/3/library/string.html#format-specification-mini-language
