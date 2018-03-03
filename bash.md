
## SSH and Networking
1. Copy contents of local directory to remote server
    `scp -r ./sourcedirectory/ username@ipaddress:~/remotedirectory`
    * if copying individual files, remove the -r option (which enables recursive copying for directories) 

## Exploring Directories
1.  Get size of directory
    `du -h your_directory`
    * du: estimate file space usage; -h option is for human readable output