# Notes on pytest

## Basic command for running test

Suppose your test file named `main_test.py` contains the following
```python
class TestClass(object):
    def test_func_1(self):
        print("Testing test_func_1!")

    def test_func_2(self):
        print("Testing test_func_2!")
```
Here are the different commands you can use in pytest:

1. Run tests and show % of tests passed: `pytest main_test.py`
2. Run tests but with verbose output: `pytest -v main_test.py`
3. Run tests but print out output to stdout: `pytest -v main_test.py -s`
4. Run only the test in test_func_1: `pytest -v exploration_test.py::TestClass::test_func_1 -s`
