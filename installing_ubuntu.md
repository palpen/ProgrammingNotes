# Installing Ubuntu

1. Download version 16.04.3 LTS of Ubuntu Desktop from the Ubuntu website
    - The file you download will be an ISO image of the operating system
2. Create a bootable USB drive on your current operating system
    - This requires using a USB stick writing tool such as Rufus
    - See this [tutorial](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows#0) for how to do this
3. Restart your computer and boot from the bootable USB drive you created in step 2. Follow the instructions on screen.
    - Good reference [here](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop#8)

## Applications to install
Before installing anything, `sudo apt-get update`

- OpenSSH (enables ssh access--see below)
- anaconda
- Vim: `sudo apt install vim`
- git: `sudo apt-get install git`
- screen (terminal multiplexer): `sudo apt-get install screen`

## Prompt customization
- Reduce prompt clutter by displaying only active virtual environment, username, and last two directories
    + Change
        `PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '`
    + to 
        `PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u:\[\033[01;34m\]\w\[\033[00m\]\$ '`
    + `\u` is your username, `\h` is the server name, which we removed
    + Also, add PROMPT_DIRTRIM=2 at the top of your .bashrc file to trim the directories shown

## Setting up SSH access
- Install OpenSSH: `sudo apt-get install openssh-server`
- then restart the service: `sudo service ssh restart`
- If you get a REMOTE HOST IDENTIFICATION HAS CHANGED! warning (and you know this is the host you want to ssh to), then delete the offending ECDSA key in ~/.ssh/known_hosts

