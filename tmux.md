# tmux Shortcuts and Cheatsheet

# Tmux man page
https://man7.org/linux/man-pages/man1/tmux.1.html

## Installing tmux

You must install tmux on the remote server you want to use it on

Homebrew
`brew install tmux`

Debian / Ubuntu
`sudo apt-get install tmux`

## Basic

Start a new tmux session:

`tmux`

A tmux session is a group of `windows`. A `window` is a group of panes. Closing a pane in a window containing only a single pane will close the window. Closing a window in a session that contains a single window will close the tmux session (even if you have multiple session instances).

To list all active sessions (and all windows attached to them), do `Prefix + s`.

To temporarily exit and subsequenty reenter a tmux session

```
(within tmux)      Prefix + d      Detach from a session  and return to shell environment
(outside of tmux)  tmux attach     Reattach previous session
```

### More tmux session commands
```
tmux new -s MY-NEW-SESSION                        Create a new named session
tmux attach-session -t SESSION-NAME
tmux rename-session -t CURRENT-NAME NEW-NAME
tmux ls                                           List all active sessions
tmux kill-session -t SESSION-NAME
tmux kill-server                                  Kill all active sessions
```

## Common Prefixed Commands

Before any of the single character shortcuts below, hit the prefix

__Control + b__

followed by the key for the desired action.

\>\> means just execute command (no need to Control + b)

### Sessions
```
:new<CR>              create new session
s                     list all active sessions (or in CLI, tmux ls)
d                     detach/leave from session
:kill-session<CR>     kills current session
$                     change session name
s                     interactively switch sessions
```

### Windows (tabs)
```
c create new window
n toggle to next window
p toggle to previous window
w interactively choose a window from across sessions
& kill / terminate current window (destroys all panes within it)
```

### Panes

```
q display pane index (useful information when swapping panes)
{ swap current pane with pane to the left index
} swap current pane with pane to the right index

% vertical split
" horizontal split

z toggle zoom in current active pane
x kill (close) pane
space toggle layout (can switch from hortizontal to vertical and vice versa)

o switch to next pane
; switch to previous pane
→, ←, ↑, ↓ move between panes

[ Scroll in pane
    * Use arrow keys to move in pane or fn + arrow key to skip a page
    * To quit scroll mode, press q

ESC + →, ←, ↑, ↓ resize panes  (must be repeated for repeated adjustment)
Hold Alt + →, ←, ↑, ↓  resize panes
```

### Package specific

```
# Resurrect
Ctrl + s  save session
Ctrl + r  restore session
```


## Joining a pane to a window
- First, break the pane to a new window with `<Prefix> !`
- Next, bind window containing the pane to the desired window with `:join-pane -t <NAME OF DESTINATION WINDOW>`
- You can use the `-h` or `-v` option in `join-pane` to bind horizontally or vertically

## Alternative way to resize panes
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
* Also see https://unix.stackexchange.com/questions/58763/copy-text-from-one-tmux-pane-to-another-using-vim

### With mouse (if current setting is `set mouse on`)
* Hold `Shift`, then drag cursor with while holding down the left mouse button, then hit the copy shortcut as usual (Command + c in MacOS).

### With keyboard
```
Prefix [ : enter copy mode (also scroll mode)
Control + Space : begin selecting block of text you want to copy
Alt + w : copy the selected text to the system clipboard
```

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

