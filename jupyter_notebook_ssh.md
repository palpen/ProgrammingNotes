# How to access a Jupyter notebook on a remote machine locally

This works only if machines are on the same network. The set up required to securely access a remote Jupyter notebook across different networks is significantly more involved.

1. ssh into the remote machine and initiate a Jupyter notebook but with the no browser option. Set any port number in the option (8889 here is arbitrary)
    - `jupyter notebook --no-browser --port=8889`
    - Note the access token when the notebook starts. This is a random sequence of characters found in the URL `http://localhost:8889/?token=ACCESS_TOKEN_HERE`
2. On a separate terminal window, create an ssh tunnel to your remote machine binding a local port to the port you set in the remote machine
    - `ssh -N -L localhost:8887:localhost:8889 $USER@$IPADDRESS`
    - Enter `localhost:8887` on your browser to access the remote Jupyter notebook
    - If you are asked for an access token, you can find it in the terminal where you activated the remote Jupyter notebook (see 1.)
    - If you get a "bind: Address already in use" error, use a different port number. It may be that you are already using that port number on a local Jupyter notebook.

## Summary
- `jupyter notebook --no-browser --port=8889` (remote)
- `ssh -N -L localhost:8887:localhost:8889 $USER@$IPADDRESS` (local)
- `localhost:8887` (local browser)

## Custom setup

Starts a jupyter lab session in remote machine and binds remote port to local port. This allows you to work on a jupyter notebook locally from a remote computer. This function will cd into the project directory, activate the specified conda environment, and initiate a jupyter lab notebook without the browser. Each step requires you to hit control + c to initiate the next step.

#### Side note
To avoid having to enter passwords, copy public key to host computer by copying LOCAL_HOME/.ssh/id_rsa.pub to a file named REMOTE_HOME/.ssh/authorized_keys

#### Requirements (on remote pc):
    1. miniconda
        - To install miniconde, do a `wget` on one of the installation urls from the [miniconda installation page](https://docs.conda.io/en/latest/miniconda.html#linux-installers) to download the installation script.
    2. JupyterLab
        - To install JupyterLab, do `conda install -c conda-forge jupyterlab` following installing of miniconda.

Copy the code below into your .bashrc or .zshrc file:

```bash
jupyssh() {
    # Usage:
    # jupyssh <project path in remote machine> <project environment name in remote machine>
    # e.g. jupyssh ~/Dropbox/data_science/fastai_deeplearning/pt1/fastai fastai

    # Information from remote computer
    USER=<USERNAME>
    IPADDRESS=<REMOTE IP ADDRESS>
    ANACONDA_PATH=/home/$USER/miniconda3

    projectpath=$1
    envname=$2

    if [ $1 = "stop" ]; then
        echo "Stopping...";
        ssh $USER@$IPADDRESS \
            "${ANACONDA_PATH}/envs/${envname}/bin/jupyter notebook stop 8889;"
        return 0
    fi

    # Find and kill process locking port 8887 in local computer
    # (in case it is being used by a previous connection that was not closed)
    lsof -ti:8887  -sTCP:LISTEN | xargs kill

    # Initializes conda environment and starts a jupyter lab session
    echo "Initialize a Jupyter Lab session"
    echo "To close session, do \"jupyssh stop ENVNAME\""

    ssh -f $USER@$IPADDRESS \
      "cd ${projectpath};
      source ${ANACONDA_PATH}/bin/activate ${envname};
      ${ANACONDA_PATH}/bin/conda env list;
      ${ANACONDA_PATH}/envs/${envname}/bin/jupyter notebook stop 8889;
      ${ANACONDA_PATH}/envs/${envname}/bin/jupyter lab --no-browser --port=8889; exit"

    # Binds the remote port 8889 to local port 8887
    echo "Open browser at http://localhost:8887"
    ssh -N -L localhost:8887:localhost:8889 $USER@$IPADDRESS
}
```

Reference: https://coderwall.com/p/ohk6cg/remote-access-to-ipython-notebooks-via-ssh

## Jupyter Notebooks on GCP Compute Engine
1. SSH into example-instance and bind remote port 5000 to the local port 2222:
    * `gcloud compute ssh example-instance -- -L 2222:localhost:5000`
    * https://cloud.google.com/solutions/connecting-securely
2. Once you are connected, run jupyter notebook in port 5000
    * `jupyter notebook --port=5000 --no-browser`
    * You can then send the running process in the background with `Control + z`, which sends it in a suspended state. To start it, enter `bg` in command line.
3. In your local machine's browser, visit http://localhost:2222/ and enter the notebook’s token to access the notebook

