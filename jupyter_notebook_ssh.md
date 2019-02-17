# How to access a Jupyter notebook on a remote machine locally

This works only if machines are on the same network. The set up required to securely access a remote Jupyter notebook across different networks is significantly more involved.

1. ssh into the remote machine and initiate a Jupyter notebook but with the no browser option. Set any port number in the option (8889 here is arbitrary)
    - `jupyter notebook --no-browser --port=8889`
    - Note the access token when the notebook starts. This is a random sequence of characters found in the URL `http://localhost:8889/?token=ACCESS_TOKEN_HERE`
2. On a separate terminal window, create an ssh tunnel to your remote machine binding a local port to the port you set in the remote machine
    - `ssh -N -L localhost:8887:localhost:8889 <username>@<server ip address>`
    - Enter `localhost:8887` on your browser to access the remote Jupyter notebook
    - If you are asked for an access token, you can find it in the terminal where you activated the remote Jupyter notebook (see 1.)
    - If you get a "bind: Address already in use" error, use a different port number. It may be that you are already using that port number on a local Jupyter notebook.

## Summary
- `jupyter notebook --no-browser --port=8889` (remote)
- `ssh -N -L localhost:8887:localhost:8889 <username>@<server ip address>` (local)
- `localhost:8887` (local browser)

## Custom setup
- see `private_work.sh` in `/Users/palermospenano/.bashrc.d`
- This function will cd into the project directory, activate the specified conda environment, and initiate a jupyter lab notebook without the browser. Each step requires you to hit control + c to initiate the next step.

```bash
jupyssh(){
    # When you provide the project folder and environment name arguements
    # this function will cd into that folder in the remote machine and
    # activate the environment for that project

    # Part 1 kills the port 8889 if already active
    # Part 2 will initialize a Jupyter Lab notebook in the remote host
    # Press Control+c to exit this ssh session and automatically
    # enter Part 3 to bind the remote port 8889 to local port 8887

    # usage: jupyssh <projectpath> <project environment name>
    # e.g. jupyssh ~/Dropbox/data_science/fastai_deeplearning/pt1/fastai fastai
    # Control + c after each part to move to next part

    projectpath=$1
    envname=$2

    # Part 1
    # note single quote: we want to pass this command in its literal form
    # to the remote machine (i.e. without evaluating $() in local machine)
    echo "Kill port 8889 if already active...(enter password follow by Control + C to move to next part)"
    ssh <USER>@<IPADDRESS> 'kill -9 $(lsof -t -i:8889); exit'
    echo ""

    # Part 2
    echo "Activate environment ${envname} and initialize a Jupyter Lab session...(enter password follow by Control + C to move to next part)"
    ssh <USER>@<IPADDRESS> "cd ${projectpath};
                                source /home/pspenano/anaconda2/bin/activate ${envname};
                                /home/pspenano/anaconda2/bin/conda env list;
                                /home/pspenano/anaconda2/envs/${envname}/bin/jupyter lab --no-browser --port=8889; exit"
    echo ""

    # Part 3: bind remote port 8889 to local port 8887
    echo "Bind remote port 8889 to local port 8887...(enter password then open new terminal window and execute jupybrowser)"
    ssh -N -L localhost:8887:localhost:8889 pspenano@192.168.0.104
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

