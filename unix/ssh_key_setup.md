# How to generate and copy public SSH key to a server

* OS: MacOS 10.14.6

If you already have a public key (`cat ~/.ssh/id_rsa.pub`), skip to step 2:

1. Generate key: `ssh-keygen -t rsa`
2. Copy key to server: `ssh-copy-id someserver@server.ip.address`

## Other info
* If `ssh-copy-id` is not installed, do `brew install ssh-copy-id`
* For detailed instructions, [click here](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)
