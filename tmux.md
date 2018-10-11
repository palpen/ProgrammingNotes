# tmux Shortcuts and Cheatsheet

## Installing tmux

You must install tmux on the remote server you want to use it on

Homebrew:
`brew install tmux`

Debian / Ubuntu
`sudo apt-get install tmux`

## Basic

Start a new tmux session:

`tmux`

## Shortcuts

Before any of the single character shortcuts below, hit the prefix

__Control + b__

followed by the key for the desired action.

\>\> means just execute command (no need to Control + b)

### Sessions
```
s list sessions
d detach/leave from session
>> tmux attach: attach to tmux session 
```

### Windows (tabs)

### Panes

```
% vertical split
" horizontal split

z toggle zoom in current active pane
x kill (close) pane

→, ←, ↑, ↓ move between panes

[ Scroll in pane 
    * Use arrow keys to move in pane or fn + arrow key to skip a page
```

## Detaching and reattaching to a session
Quoting answer in https://askubuntu.com/a/220880 below

1. ssh into the remote machine
2. start tmux by typing `tmux` into the shell
3. start the process you want inside the started tmux session
4. leave/detach the tmux session by typing `Ctrl+b` and then `d`

You can now safely log off from the remote machine, your process will keep running inside tmux. When you come back again and want to check the status of your process you can use `tmux attach` to attach to your tmux session.

If you want to have multiple sessions running side-by-side, you should name each session using `Ctrl+b` and `$`. You can get a list of the currently running sessions using `tmux list-sessions`, now attach to a running session with command `tmux attach-session -t 0`.

## Useful scripts
* Create new session, split panes, and cd into desired directory for each pane
```
tmux new-session \; split-window -h -c ~/path/to/dir1 \; split-window -v -c ~/path/to/dir2 \; attach
```

## Good Reference
* https://gist.github.com/MohamedAlaa/2961058

