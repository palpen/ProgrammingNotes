
# Notes on Spacemacs

## Getting Started

For installation instructions, [click here](https://github.com/syl20bnr/spacemacs#install). Note that one must first install Emacs before Spacemacs

Starting spacemacs, run

```
emacs --insecure
```

## Commands

### Key Definitions

```
C -> Control
M -> Meta (Option)
SPC -> Space (unique to Spacemacs)
	Easier way to access useful commands and other functionalities (e.g. shell command)
```

### Basic commands

```
C-x C-c -> Quit emacs
C-g -> Cancel current action
C-x C-f -> Open a file (whether or not it exist)
C-x C-s -> Save file
C-x C-w -> Write a file (Save as...)

# Emacs commands (M-x)
cd -> Change working directory of current session
pwd -> Print current directory
```

### Buffers and Windows

```
C-x 0 -> Undo window splitting and return to one window
C-x C-+/- -> Zoom in/out text
C-x leftArrow / rightArrow -> Switch to previous / next buffer in current window
C-x o -> Go to other window (other-window)
C-x k -> Kill current buffer
```

### Standard ML specific commands

```
C-c C-s -> Open SML prompt
C-c C-d -> End SML session (comint-send-eof)
C-c C-n -> Go to next prompt (useful when an error is raised and want to close end session)
C-c C-o -> Delete output
M-; -> Apply line comment to selected line
```

### Spacemacs specific commands
```
SPC s c -> Clear search highlight
SPC T M -> Maximize frame (window take up full height of screen)
```

### Misc. Commands
M-x, then search `delete-trailing-whitespace` -> Removes all trailing whitespace

## Configuring Spacemacs

Spacemacs can be customized using ``~/.spacemacs``

* How to change default font
```
 dotspacemacs-default-font '("Source Code Pro"
                               :size 17
                               :weight normal
                               :width normal
                               :powerline-scale 1.1)
```
* Add line numbers: `dotspacemacs-line-numbers t`
* How to make window use 100% of screen. Add `frame-resize-pixelwise t` in `setq-default`:
```
(setq-default
 frame-resize-pixelwise t
 ...
)
```

## Resources
- [A Guided Tour of (original) Emacs](https://www.gnu.org/software/emacs/tour/index.html)
