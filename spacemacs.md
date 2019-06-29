
# Notes on Spacemacs

Starting spacemacs, run

```
emacs --insecure
```

## Key combinations
C -> Control
M -> Meta (Option)

C-c C-s -> Open SML prompt
C-c C-d -> end SML session (comint-send-eof)

C-x C-c -> Quit emacs
C-g -> Cancel current action
C-x C-f -> open a file (whether or not it exist)
C-x C-s -> Save file
C-x C-w -> Write a file (Save as...)

C-x 0 -> Undo window splitting and return to one window
C-x C-+/- -> Zoom in/out text


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
