# Notes on Flask

## How to define a route
```python
@app.route('user/<username>')
def profile(username):
    print(f"Username is {username}")
```

## How to run application in debugger mode
Export the `FLASK_DEBUG` environmental variable (after exporting `FLASK_APP` before executing `flask run`

```
$ export FLASK_APP=hello.py
$ export FLASK_DEBUG=1
$ flask run
```
where `hello.py` is your main python script containing your view functions. This let's you update the application automatically while working on the code
