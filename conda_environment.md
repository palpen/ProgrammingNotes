## Virtual environments using conda

### How to create a new environment and open an ipython notebook in it
- Create a virtual environment using python 2.7 and install some packages
    + `conda create -n udacity_ml_titanic python=2.7 numpy pandas matplotlib scikit-learn`
- Activate environment
    + `source activate udacity_ml_titanic`
- Install ipython notebook in new environment
    + `conda install ipython-notebook`
    + Alternatively, you can install the notebook extension that allows you to switch kernels into your various environments
        * `conda install nb_conda`
        * I wonder if you can just install this in root and not have to install it every time you create a new environment ???
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
- Follow with installation of extension to let you switch environments within a jupyter notebook: `conda install nb_conda`
- Reactivate virtual environment

### Checking the program file in user path
To check that the python or jupyter notebook you are using is indeed the one installed inside your environment, use the `which` command
- `which python`
- `which ipython`
- `which jupyter`

To see a list of all the packages installed under an environment, `ls /Users/USERNAME/anaconda2/envs/MY_ENVIRONMENT`

### How to list and check currently active environments
- `conda info --envs`

### How to export environment into a .yml file
Not a great idea if this is going to be used to create an environment in another operating system (see best practices below)
- `conda env export > environment.yml`

### Conda environment and TensorFlow
- TensorFlow on CPU
    + create conda environment using the yml file, but don't include tensorflow in the file
    + Once the environment is set up and activated, install tensorflow following command: `conda install -c https://conda.anaconda.org/jjhelmus tensorflow`
        * https://stackoverflow.com/questions/46382909/tensorflow-is-not-working-on-a-conda-environment
- TensorFlow on GPU (machine with a GPU)
    - Create the environment, again using the yml file but making sure it does not have TensorFlow
    - In the activated environment, `pip uninstall tensorflow` (this should have been installed along with keras)
    - Then install the GPU version of TensorFlow: `pip install tensorflow-gpu`

### How to delete an environment
- `conda remove --name flowers --all`

### Automatically activate an environment when you cd into it
- Install autoenv: `pip install autoenv && source activate.sh`
- Create a .env file with `source activate <env name>` in it inside the folder containing the code for the virtual environment
- Now every time you enter that folder from the command line the virtual environment will be activated.

### Virtual environment best practices
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