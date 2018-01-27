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

Reference: https://coderwall.com/p/ohk6cg/remote-access-to-ipython-notebooks-via-ssh
