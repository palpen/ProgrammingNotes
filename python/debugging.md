# Notes on Debugging, Debuggers in Python

## pdb
Insert `import pdb; pdb.set_trace()` in line where you want debugging to start.


## Commands:
* l: list code snippet
* n: line by line execution
* b <NUM>: insert a breakpoint at line <NUM>
* c: continue until end or reach breakpoint
* b <LINE NUM>, <CONDITION>: conditional breakpoints
    * e.g `b 69, length != sum(aa_counts)`

## Resources
1. [Python Debugging With Pdb](https://realpython.com/python-debugging-pdb/)
2. [ipdb: an improved version of pdb](https://pypi.org/project/ipdb/)
3. [PyData Video on Debugging Python Programs](https://www.youtube.com/watch?v=04paHt9xG9U)
    * [github repo](https://github.com/krother/debugging_tutorial)
