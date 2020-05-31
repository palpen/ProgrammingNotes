# tmux Shortcuts and Cheatsheet

## Installing tmux

You must install tmux on the remote server you want to use it on

Homebrew
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
s list all active sessions (or in CLI, tmux ls)
d detach/leave from session
:kill-session kills current session
$ change session name
```

Manipulating sessions from the shell,
```
tmux attach-session -t [SESSION-NAME]
tmux rename-session [-t CURRENT-NAME [NEW-NAME]
tmux ls --> List all active sessions
```
### Windows (tabs)
```
c create new window
n toggle to next window
p toggle to previous window
w interactively choose a window from across sessions
```

### Panes

```
% vertical split
" horizontal split

z toggle zoom in current active pane
x kill (close) pane

o switch to next pane
→, ←, ↑, ↓ move between panes

[ Scroll in pane
    * Use arrow keys to move in pane or fn + arrow key to skip a page
    * To quit scroll mode, press q

ESC + →, ←, ↑, ↓ resize panes  (must be repeated for repeated adjustment)
```

#### Alternative way to resize panes
```
:resize-pane -D 10
:resize-pane -U 10
:resize-pane -L 10
:resize-pane -R 10
```

To equally balance layout of panes:
```
:select-layout even-vertical
:select-layout even-horizontal
```

## Copy / Pasting in tmux
* See https://awhan.wordpress.com/2010/06/20/copy-paste-in-tmux/

## Killing Sessions
There are various ways:
* From within session you want killed: `Control + b, :, then type 'kill-session'`
* If you know the id of the sesssion you want dead: `tmux kill-session -t targetSession`
   * Use `tmux list-sessions` to list all active sessions and their ids


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

