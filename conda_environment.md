## Virtual environments using conda

### How to create a new environment and open an ipython notebook in it
- Create a virtual environment using python 2.7 and install some packages
    + `conda create -n udacity_ml_titanic python=2.7 numpy pandas matplotlib scikit-learn`
- Activate environment
    + `source activate udacity_ml_titanic`
- Install ipython notebook in new environment
    + `conda install ipython-notebook`
- Deactivate then reactivate the environment to detect new installation of ipython notebook
- After reactivating the notebook, use `jupyter notebook` command to open the notebook
- check python version to confirm  version installed is 2.7
    ```
    import sys
    sys.version
    ```

### How to clone a virtual env.
- `conda create --name <name of cloned env> --clone <env I want to clone>`

### How to create virtual environment using a yml file
- Install anaconda environment
    - `conda env create -f environment.yml`
    - An example of the contents of a yml file containing dependencies is as follows:

    ```
    name: uber_env
    dependencies:
    + mkl=11.3.3=0
    + numpy=1.11.1=py27_0
    + openssl=1.0.2h=1
    + pandas=0.18.1=np111py27_0
    + patsy=0.4.1=py27_0
    + pip=8.1.2=py27_0
    + python=2.7.12=1
    + scikit-learn=0.17.1=np111py27_2

    prefix: /Users/bjherger/anaconda2/envs/uber_env
    ```

### How to list and check currently active environments
- `conda info --envs`

### How to export environment into a .yml file
Not a great idea if this is going to be used to create an environment in another operating system (see best practices below)
- `conda env export > environment.yml`

### How to delete an environment
- `conda remove --name flowers --all`

### virtual environment best practices
Create environment.yml file by hand. Here's an example

```
name: toxic_comment_kaggle
dependencies:
  - python=3.5
  - pandas
  - numpy
  - matplotlib
  - scikit-learn
  - keras
  - ipython-notebook
```

This way, you let conda deal with the dependencies required for each of these packages. Also, you reduce the likelihood of an error when creating this environment on a different operating system

- https://stackoverflow.com/questions/39280638/how-to-share-conda-environments-across-platforms
- https://github.com/conda/conda/tree/master/conda_env

Reference: https://conda.io/docs/user-guide/tasks/manage-environments.html