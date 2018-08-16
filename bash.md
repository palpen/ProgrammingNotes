
## Basic Operations
1. Declare an array and loop through its contents
```bash
declare -a arr=("e1" "e2" "e3")

for i in "${arr[@]}"
do
    echo "$i"
done
```
Note arr[0] corresponds to the element "e1". Using @ (or \*), expands the contents of the array, allowing us to use it as an object to iterate over.


## SSH and Networking
1. Copy the `sourcedirectory` folder from local directory to `remotedirectory` folder in the remote server:
    `scp -r ./sourcedirectory/ username@ipaddress:~/remotedirectory`
    * If copying individual files, remove the -r option (which enables recursive copying for directories)
2. List all network open ports:
    `lsof -i`
3. Get IP address of localhost:
    `ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`
    * See https://stackoverflow.com/questions/13322485/how-to-get-the-primary-ip-address-of-the-local-machine-on-linux-and-os-x

## Exploring and Manipulating Directories
1.  Get size of directory:
    `du -h your_directory`
    * du: estimate file space usage; -h option is for human readable output

2. Create a symbolic link:
    `ln -s /path/to/original/directory/or/file name_of_link`
    * This creates a "folder" named `name_of_link` that you can use to access contents of `/path/to/original/directory/or/file`
    * To destroy the link, `rm name_of_link`

3. `cd`, `pushd`, `popd`, and `dirs -v`
    * Say you have several directories you need to navigate over. To navigate to and "save" the directories in a directory stack, `pushd mydir`
    * To see directories in current stack: `dirs -v`
    * To navigate to a directory in the current stack: `cd ~DIR_NUM` where `DIR_NUM` is the number assigned to directory you want to go to
    * You must always save the most recent folder in the stack twice as the folder assigned to zero will always be replaced
    * See https://unix.stackexchange.com/a/270437/87545 for details

## System stuff
1. Check if drive is mounted: `lsblk`
    * If it doesn't have a mount point it is not mounted. To mount it, execute `udisksctl mount -b /dev/sdb1`  where `/dev/sdb1` is the disk you want to mount
    * In my case, the mount point becomes `/media/pspenano/2TB\ HDD`
