# How to access a jupyter notebook on a remote machine locally

1. ssh into the remote machine and initiate a jupyter notebook but with the no browser option. Set any port number in the option (8889 here is arbitrary)
    - `jupyter notebook --no-browser --port=8889`
    - Note the access token when the notebook starts. This is a random sequence of characters found in the URL `http://localhost:8889/?token=ACCESS_TOKEN_HERE`
2. On a separate terminal window, create an ssh tunnel to your remote machine binding a local port to the port you set in the remote machine
    - `ssh -N -f -L localhost:8888:localhost:8889 <username>@<server ip address>`
    - Enter `localhost:8888` on your browser to access the remote jupyter notebook