# Notes on Exception Handling

## 1.
```python
try:
    foo(x)
except Exception as e:
    print("An exception was raised:", e)
```

Execute the function `foo`, if an exception is raised, print out captured exception to standard output.

## 2.
```python
try:
    foo(x)
except Exception as e:
    print("An exception was raised:", e)
else:
    bar(x)
```

Execute function `foo` and if no exception is raised, execute `bar`. If an exception is raised, `bar` will not be executed and the captured exception will be printed to standard output.

## 3.
```python
try:
    foo(x)
except Exception as e:
    print("An exception was raised:", e)
finally:
    final_bar(x)
```

Same as 2., except the function `final_bar` is executed whether or not an exception was raised. `foo` could be a long-running process the result of which we want to export to a csv file. We don't want to start over in case it gets interrupted, so we execute `final_bar` to save the results we have.

## 4.
```python
try:
    foo(x)
except Exception as e:
    print("An exception was raised:", e)
else:
    bar(x)
finally:
    final_bar(x)
```

Execute `foo`, if an exception is raised, print exception then execute `final_bar`. If no exception is raised, execute `bar` followed by `final_bar`