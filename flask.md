# Notes on Flask

## How to define a route
```python
@app.route('user/<username>')
def profile(username):
    return f"Username is {username}"
```

When this app is running, executing `curl http://127.0.0.1:5000/user/johnsmith` will return "Username is johnsmith". To filter by type before passing into the view function

```python
@app.route('user/id/<int:user_id>')
def profile(user_id):
    return f"The user id is {user_id}"
```

## How to run application in debugger mode
Export the `FLASK_DEBUG` environmental variable (after exporting `FLASK_APP` before executing `flask run`

```
$ export FLASK_APP=hello.py
$ export FLASK_DEBUG=1
$ flask run
```
where `hello.py` is your main python script containing your view functions. This let's you update the application automatically while working on the code
