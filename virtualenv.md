# virtualwrapper
`virtualwrapper` is a set of extensions for the `virtualenv` tool. It makes it easier to work with `virtualenv`.

`virtualenv` this is just another way to create a virtual environment. The alternative is to use `conda`. Creating a virtual environment using `virtualenv` is desirable if you are working on a server where it would be infeasible to install Anaconda.

## Installing virtualenvwrapper:
- Issues when python installed through Anaconda. Issue arises when `virtualenv` is installed using `pip` under a Python distribution that `conda`.
    - Resolved here: https://stackoverflow.com/questions/5904319/problem-with-virtualenv-in-mac-os-x

## Common commands
- `mkvirtualenv`: create a new virtualenv
- `lsvirtualenv`: -b option gives brief list of all virtualenv, -l for long
- `rmvirtualenv`: remove an existing virtualenv
- `workon`: change the current virtualenv
- `add2virtualenv`: add external packages in a .pth file to current virtualenv
- `cdsitepackages`: cd into the site-packages directory of current virtualenv
- `cdvirtualenv`: cd into the root of the current virtualenv
- `deactivate`: deactivate virtualenv, which calls several hooks

## Check if inside a virtual environment
`python -c 'import sys; print("In virtuaenv" if hasattr(sys, "real_prefix") else "Not in virtenv")'`
- reference: https://stackoverflow.com/questions/15454174/how-can-a-shell-function-know-if-it-is-running-within-a-virtualenv
- Alias in my system `checkve`

## Location of virtualenvironments
- /Users/palermospenano/.virtualenvs