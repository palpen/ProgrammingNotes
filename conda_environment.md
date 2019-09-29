# Virtual environments using conda

### Quickly create an environment and activate it
```shell
conda create -n myenv python=3.7
conda activate myenv
```

### How to create virtual environment using a list of packages from a yml file
- Create a file named `environment.yml` similar to the example below:
    ```
    name: myenv
    dependencies:
      - python=3.7
      - pandas
      - numpy
    ```
- Create the environment with by executing
    `conda env create -f environment.yml`
    - If you are in the directory where `environment.yml` lives, just run `conda env create`
- Activate the environment with `conda activate myenv`

### Pip install in conda
See note below on __Setting channels in environment file__ for an alternative approach

In `environment.yml` file, do the following:
```
name: toxic_comment_kaggle
dependencies:
  - pip
  - pip:
    - flask_restplus
```

### How to clone a virtual environment
- `conda create --name <name of cloned env> --clone <env I want to clone>`

### How to list and check currently active environments
- `conda env list`

### How to export environment into a .yml file
- Not a great idea if this is going to be used to create an environment in another operating system (see best practices below)
- Specifically, the package versions exported using this approach may not exist in an operating system different from the one where the environment was originally created
- If you insist in doing this, the command is `conda env export > environment.yml`

### How to delete an environment
- `conda remove --name flowers --all`

### Automatically activate an environment when you cd into it
- Install autoenv: `pip install autoenv && source activate.sh`
- Create a .env file with `source activate <env name>` in it inside the folder containing the code for the virtual environment
- Now every time you enter that folder from the command line the virtual environment will be activated.

### Virtual environment best practices
- Environments should be 
- References:
  - https://stackoverflow.com/questions/39280638/how-to-share-conda-environments-across-platforms
  - https://github.com/conda/conda/tree/master/conda_env
  - https://conda.io/docs/user-guide/tasks/manage-environments.html

### Setting channels in environment file
Occasionally, the package you need is not available in the default [channel](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html) used by the conda package manager. To set the channel from which to install your package, list them under a `channels` heading in your environment yaml file:

```
name: myenv
channels:
  - defaults
  - conda-forge
dependencies:
  - flask_restplus
```

`conda-forge` contains packages that may not be in the Anaconda repository of packages. Specifying this channel will allow you to install such packages that do not exist in the default channel.

Sometimes there are issues with installing packages using different package managers in the same environment. One example is when one uses pip inside an environment create by conda. To avoid these issues, don't install the package using pip if you are creating an environment using conda. Instead, look for the channel in which a package lives and specify the channel in the yaml file (as shown in the example above).


## Package-specific instructions

### Conda environment and TensorFlow
- TensorFlow on CPU
    + create conda environment using the yml file, but don't include tensorflow in the file
    + Once the environment is set up and activated, install tensorflow following command: `conda install -c https://conda.anaconda.org/jjhelmus tensorflow`
        * https://stackoverflow.com/questions/46382909/tensorflow-is-not-working-on-a-conda-environment
- TensorFlow on GPU (machine with a GPU)
    - Create the environment, again using the yml file but making sure it does not have TensorFlow
    - In the activated environment, `pip uninstall tensorflow` (this should have been installed along with keras)
    - Then install the GPU version of TensorFlow: `pip install tensorflow-gpu`
