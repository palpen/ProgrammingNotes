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

## Good Reference
* https://gist.github.com/MohamedAlaa/2961058

