# Notes on bash and shell

## Shortcuts
Alt + d -> Delete one word forward

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

## Background Processes
See: https://www.blockloop.io/mastering-bash-and-terminal/
1. ctrl-z - move the current process to the background in a suspended state.
2. jobs -l - list the current background processes for the current tty session.
3. bg - tell the most recent background process to continue running in the background
4. fg - bring the most recent background process back to the foreground
5. disown -h - disown the most recent background job. This will remove it from your current tty session. It will not be able to be brought back to the foreground. You will have to control it either with kill or something else.
6. To kill a running process, find job number and execute `kill %<JOB_NUMBER>` ([source](https://unix.stackexchange.com/questions/104821/how-to-terminate-a-background-process/104825)):
    ```
    $ jobs
    [1]+  Running                 my_script.py

    $ kill %1
    [1]+  Terminated              my_script.py
    ```

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
1.  Storage usage information for directory:
    `du -h your_directory`
    * du: estimate file space usage; `-h` option is for human readable output
    * Use `-s` option for total for directory

2. Get free disk space information for directory: `df .`

3. Create a symbolic link:
    `ln -s /path/to/original/directory/or/file name_of_link`
    * This creates a "folder" named `name_of_link` that you can use to access contents of `/path/to/original/directory/or/file`
    * To destroy the link, `rm name_of_link`

4. `cd`, `pushd`, `popd`, and `dirs -v`
    * Say you have several directories you need to navigate over. To navigate to and "save" the directories in a directory stack, `pushd mydir`
    * To see directories in current stack: `dirs -v`
    * To navigate to a directory in the current stack: `cd ~DIR_NUM` where `DIR_NUM` is the number assigned to directory you want to go to
    * You must always save the most recent folder in the stack twice as the folder assigned to zero will always be replaced
    * See https://unix.stackexchange.com/a/270437/87545 for details

5. How to use `find` to list only files following a given pattern
    * `find . -name "*Pattern*"`

6. How to use `find` with `-exec` option
    * `find . -name "*.log" -exec echo {} \;`
        - Searches current directory for files matching `*.log` and passes each file name as an argument to `echo`
        - Replacing `\;` with `+` will, instead, pass as many of the parameters as possible to `echo`
    * Using child shell, `sh -c`, with `find` and `-exec`
        - To pass argument to child shell: `sh -c 'echo  "You gave me $1, thanks!"' sh "apples"`
        - The second `sh` goes to `$0` and will be used in the shell's error message
        - To use together to change the extension of files in `.` from `.text` to `.txt`
        ```bash
        from=text  #  Find files that have names like something.text
        to=txt     #  Change the .text suffix to .txt

        find . -type f -name "*.$from" -exec sh -c 'mv "$3" "${3%.$1}.$2"' sh "$from" "$to" {} ';'
        # Copied from https://unix.stackexchange.com/a/389706/87545
        ```
        - Good references
            - https://unix.stackexchange.com/a/156010/87545

7. Search all occurence of a given pattern across all files in a directory
    * `grep -HirIn "pattern" .`
    * Searches for `pattern` in the current directory.
    * `H` always shows the filename. `i` makes the pattern case insensitive. `r` searches does a recursive search of the directory. `I` ignores binary files. `n` prints the line number within each file where the pattern was found.

## System stuff
1. Check if drive is mounted: `lsblk`
    * If it doesn't have a mount point it is not mounted. To mount it, execute `udisksctl mount -b /dev/sdb1`  where `/dev/sdb1` is the disk you want to mount
    * In my case, the mount point becomes `/media/pspenano/2TB\ HDD`

## Other useful commands

* Sampling data from the command line

```bash
head -n1 fulldata.csv > sampled_data.csv
tail -n+2 fulldata.csv | shuf -n 100000 >> sampled_data.csv
```

First line writes the header; the second line samples the file (excluding the header)


