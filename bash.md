
## SSH and Networking
1. Copy contents of local directory to remote server:
    `scp -r ./sourcedirectory/ username@ipaddress:~/remotedirectory`
    * If copying individual files, remove the -r option (which enables recursive copying for directories)
2. List all network open ports:
    `lsof -i`

## Exploring and Manipulating Directories
1.  Get size of directory:
    `du -h your_directory`
    * du: estimate file space usage; -h option is for human readable output

2. Create a symbolic link:
    `ln -s /path/to/original/directory/or/file name_of_link`
    * This creates a "folder" named `name_of_link` that you can use to access contents of `/path/to/original/directory/or/file`
    * To destroy the link, `rm name_of_link`

## System stuff
1. Check if drive is mounted: `lsblk`
    * If it doesn't have a mount point it is not mounted. To mount it, execute `udisksctl mount -b /dev/sdb1`  where `/dev/sdb1` is the disk you want to mount
    * In my case, the mount point becomes `/media/pspenano/2TB\ HDD`

