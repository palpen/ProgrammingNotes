# Notes on networking on Linux


# SSH

## Set up new Linux pc for ssh access
1. On the linux pc, install openssh-server and openssh-client
    - `sudo apt-get install openssh-server openssh-client`
2. Get the private ip address of the pc in your local network
    - In the terminal, enter `ip a | grep inet`
    - You'll see severl output but select the ip address next to inet, particularly the one with a `global` scope
3. Test the connection using the ip from above and the username of the linux pc
    - `ssh linuxpcusername@ipaddress`


## How to generate and copy public SSH key to a server

* OS: MacOS 10.14.6

If you already have a public key (`cat ~/.ssh/id_rsa.pub`), skip to step 2:

1. Generate key: `ssh-keygen -t rsa`
2. Copy key to server: `ssh-copy-id someserver@server.ip.address`

## Other info
* If `ssh-copy-id` is not installed, do `brew install ssh-copy-id`
* For detailed instructions, [click here](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)
