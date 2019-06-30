
# Notes on Spacemacs

Starting spacemacs, run

```
emacs --insecure
```

## Commands

### Key definitions
C -> Control
M -> Meta (Option)

### Basic commands
C-x C-c -> Quit emacs
C-g -> Cancel current action
C-x C-f -> open a file (whether or not it exist)
C-x C-s -> Save file
C-x C-w -> Write a file (Save as...)

### Buffers and Windows
C-x 0 -> Undo window splitting and return to one window
C-x C-+/- -> Zoom in/out text
C-x leftArrow / rightArrow -> Switch to previous / next window in buffer
C-x k -> Kill current buffer

### Standard ML specific commands
C-c C-s -> Open SML prompt
C-c C-d -> end SML session (comint-send-eof)

## Configuring Spacemacs

__How to change default font__
Look for

```
 dotspacemacs-default-font '("Source Code Pro"
                               :size 17
                               :weight normal
                               :width normal
                               :powerline-scale 1.1)
```

`~/.spacemacs` edit the `size` parameter
