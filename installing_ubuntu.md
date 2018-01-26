# Installing Ubuntu

1. Download version 16.04.3 LTS of Ubuntu Desktop from the Ubuntu website
    - The file you download will be an ISO image of the operating system
2. Create a bootable USB drive on your current operating system
    - This requires using a USB stick writing tool such as Rufus
    - See this [tutorial](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows#0) for how to do this
3. Restart your computer and boot from the bootable USB drive you created in step 2. Follow the instructions on screen.
    - Good reference [here](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop#8)

## Applications to install
- OpenSSH (see below)
- Vim: `sudo apt install vim`

## Setting up SSH access
- Install OpenSSH: `sudo apt-get install openssh-server`
- then restart the service: `sudo service ssh restart`
- If you get a REMOTE HOST IDENTIFICATION HAS CHANGED! warning (and you know this is the host you want to ssh to), then delete the offending ECDSA key in ~/.ssh/known_hosts

