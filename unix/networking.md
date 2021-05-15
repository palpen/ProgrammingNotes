# Notes on networking on Linux


# SSH

## Set up new Linux pc for ssh access
1. On the linux pc, install openssh-server and openssh-client
    - `sudo apt-get install openssh-server openssh-client`
2. Get the private ip address of the pc in your local network
    - In the terminal, enter `ip a | grep inet`
    - You'll see a multiline output but select the ip address next to the line that begins with inet, particularly the one with a `global` scope
3. Test the connection using the ip from above and the username of the linux pc
    - `ssh linuxpcusername@ipaddress`


## How to generate and copy public SSH key to a server

* OS: MacOS 10.14.6

If you already have a public key (`cat ~/.ssh/id_rsa.pub`), skip to step 2:

1. Generate key: `ssh-keygen -t rsa`
2. Copy key to server: `ssh-copy-id someserver@server.ip.address`

# Steps to set up remote ssh access outside local network
- Enable port forwarding in router and set the server to listen to that port
    - Choose a port number, say 22342
- On server, install openssh-client and openssh-server
- Do `sudo vim /etc/ssh/sshd_config` and the port you added to your router’s settings
    - Port 22342
    - Test that sshd_config does not contain errors
        - sudo sshd -t
- Restart ssh service with `service sshd restart`
- Check that the server is listening to that port
    - sudo netstat -ltnp | grep ssh
    - sudo lsof -i -n -P | grep LISTEN
    - You should see the port number in the output
- Get the IPv4 address of the router (https://www.whatismyip.com/)
    - Call this ROUTER_IP
- Connect using the port number in the example
    - ssh -p 22342 SERVER_USERNAME@ROUTER_IP
- Copy ssh public ssh keys and test connection with keys
    - Do this before disabling password login!!!
- Secure ssh access (config for the server PC)
    - Use a large port number
    - Disable password login (must use key pairs for authentication)
        - In /etc/ssh/sshd_config, loog for `PasswordAuthentication` and change it to `PasswordAuthentication no`
    - Disable Server SSH Root Login
        - https://phoenixnap.com/kb/linux-ssh-security#htoc-4-disable-password-based-logins-on-your-server

## Other info
* If `ssh-copy-id` is not installed, do `brew install ssh-copy-id`
* For detailed instructions, [click here](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)
