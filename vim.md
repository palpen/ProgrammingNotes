# Notes on Vim

[My vimrc file](https://github.com/palpen/config_files/blob/master/.vimrc)

# Don't use Vim, use NeoVim
* When using the Alacritty terminal, NeoVim seems to respect the terminal's color setting out of the box.

## Saving vim sessions

Saves all the windows and open files (and buffers?) after closing vim so that you can recover the same setup again next time [Source](https://jvns.ca/blog/2017/09/10/vim-sessions/)

* Make session: `mks ~/.vim/sessions/mysession.vim`
* Open a session
    * In Vim, `:source ~/.vim/sessions/mysession.vim`
    * In a terminal, `vim -S ~/.vim/sessions/mysession.vim`

## Motion
Reference: [Text-object selection](http://vimdoc.sourceforge.net/htmldoc/motion.html#object-select)
* Select a word: `viw`
* Select contents inside braces: `vib`
* Select contents inside quotes: `vi<QUOTE CHARACTER>`
    * `vi"`
* Move cursor to previous or next empty line: `}` or `{`
* [Indent multiple lines quickly](https://stackoverflow.com/questions/235839/indent-multiple-lines-quickly-in-vi): `>>` (shift + . + .)
* Insert # in front of _selected_ lines. [Stackoverflow answer](https://stackoverflow.com/a/253391):
	* `Control + v` to enter columnwise visual mode
	* Select desired lines
	* `Shift + i` to enter insert mode on those lines and insert #
	* Escape to apply changes to the selected lines

## Scrolling

* Recenter the line that the cursor is on: `zz`
* Scroll up or down: `Control + u` or `Control + d`
    * To scroll one line at a time, use `e` or `y` instead

## Visual Mode
* Enter visual mode: `v`
* Visually select entire line: `Shift +v`
* Start visual mode with the same area selected in previous operation: `gv`

## Command mode
* To enter command mode, do `:` in normal mode
* To see a list of previously run commands, `q:`
    * To run it, place your cursor on the command and hit enter
    * To quit it, `:q`
* To run a bash command in command mode, use `!`
    * Say you want to align a visually selected group of text using the `column` command in bash. Visually select the text then do `:'<,'>!column -t`
* `:%` means the entire file
    * so `:%s/foo/bar/g` means to replace all instance of foo with bar in file

## Moving within a line (left-right motions)
* Bring cursor to a character: `f<CHAR>`
* Bring cursor _before_ a character: `t<CHAR>`
    * This is useful for deleting up to a charcter (say deleting the remaining contents of a list without deleting the final brace with `dt]`, where <CHAR>==`]`)

## Deletion and insertion
* `S` or `cc` to delete current line and enter insert mode.
    * `3S` deletes the next 3 lines
    * `set autoindent` to start insert mode at the end of indentation
* D -> delete from cursor to end of line (characterwise)

### Inserting a line in the middle of another line
`dd` will do a linewise deletion, which following a put command, `P` or `p`, will either insert the deleted line before or after the line in which the cursor is located. To insert the deleted line at the cursor position, do a characterwise deletion, `0D` (0 will move cursor to the begining of the line and `D` will do a characerwise deletion from the cursor to the end of the line). See https://vimhelp.org/motion.txt.html#linewise

## Exploring the file system from within Vim

* Explore file system and open a file in current viewport split: `:Ex`
* Create a split first then explore the file system
    * `:Sex`, `:Vex`, `Tex` for horizontal, vertical, and tab splits
* To exit the file exploration interface, do `:q`

Source: https://stackoverflow.com/questions/1445992/vim-file-navigation

## Tabs

Tabs are useful for working on a seperate part of the project without messing with your current view. For example, you can have files from folder `foo/` opened across multiple windows in one tab and files from folder `bar/` opened in an another tab.

* Create a new window in a new tab, `:tabnew`
* Previously accessed tab, `g<Tab>`
* Cycle through tabs, `gt`
* Access the tab in position [count], `[count]gt`
* List all windows within each tab, `:tabs`
* Close current tab (and all windows in it), `:tabc`
* For more information, `:help tab-page-commands`

## Buffers
vims way of editing multiple files within the same vim session.

* To open a file in the same vim session, do `:e <FILENAME>`
* To list files in the buffer, do `:ls`
* To toggle across files in the buffer, do `:b <TAB>`
    * One can also type name of the file in the buffer or its number
    * `:b myfile.py` or `:b 2`
* To toggle / switch between current and previous buffer, do `Control + 6`
* Remap Control + j or k to toggle buffers (see .vimrc file)
* To close all buffers at once, do `:qa`

## Viewport navigation ("Windows")
* To create a new window `Control + w, n` (to close it, `:q`)
* To do a vertical split `:vsp` (for horizontal, `:sp`)
* To navigate across splits, do `Control + w` then `h, j, k, or l`
* To close all split and focus on current split
* To zoom into current active viewport split
    * vertical split, `Control + w, |`
    * horizontal split, `Control + w, _`
* To equalize the splits, `Control + w, =`

## Search and replace
* Place a # in front of every line: `:%s/^/#/`
* Place a , at the end of every line: `:%s/$/,/`
* Using `gn` to change text that match the current search pattern
    * Search the word using `/`
    * In normal mode, do `cgn` to change matched text under cursor
    * To change subsequent matches, hit `.` (no need to hit `n`)

## Code folding
* To fold a block of code, visually select the code to fold and do `zf`
* To unfold at the cursor, do `zo`
* To unfold all folds in file, do `zR`

## Convert a comma-delimited row of text into a column (and vice versa)

```
a,b,c,d,e,f,g
```

- Visually select row with `Shift + v`
- Then in `:` mode, do `s/,/,\r/g`. `\r` is for carriage return.
- Specifically, `:'<,'>s/,/,\r/g`

```
a,
b,
c,
d,
e,
f,
g

```
- To convert back to a row, visually select block of text with `Control +V`, then go to end of line with `$`
- In `:` mode, do `s/\n//g`

## Other Commands and shortcuts
* How to comment / uncomment out a block of code: https://stackoverflow.com/a/23063140/3649966
* Copy to clipboard
    * Visually select segment to copy, then `:w !pbcopy`
* Display name of current file: `Control + g`
* Search for word under cursor (in vim): place cursor on word then press, * (`Shift + 8`)
* Delete character across visually selected group of text spanning multiple lines
    * https://stackoverflow.com/a/48952069/3649966
    * Use visual-block to highlight lines, then ":", then "%normal $x", then hit enter
* Leader key: By default it is `\`, but it may be mapped to `,`. Search the `.vimrc` file for `mapleader`.
* Aligning a column of text: Visually select the column then do `:'<,'>!column -t`
* Clear all highlighted elements (following a search query, for example): `, + n`
    * `,` has been mapped to the leader key in your `.vimrc`

## Preview markdown files
* Install the Google Chrome browser
* Install the MarkDown Preview Plus extension on Chrome (follow usage instructions)
    * https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl
    * Chrome > Preferences > Extensions > Markdown Preview Plus > Enable `Allow access to file URLs`
* in Vim, open markdow file by `:!open -a /Applications/Google\ Chrome.app mymarkdownfile.md`


## Macros

For complicated edits involving multiple lines of variable lengths, use macros. For example, suppose you wanted to enclose the text before the colon in quotes and add a comma at the end to turn it into a dictionary

```
var: 1
longvar: 2
verylongvar: 3
```

Record a macro that applies the desired operations on the first line, then apply the recorded macro on the subsequent lines by visually selecting those lines and doing `'<,'> norm @q` where `q` is the register where the macros is stored.

The sequence of characters when recording would be

```
qq
^i"f:i",
q
```

`i"` enters insert mode; `f:` finds the double colon and takes the cursor there; `i", inserts the final quote and the comma at the end of the line.

The final `q` stops the recording. Finally, visually select the subsequent lines and do

```
:'<,'>norm @q
```

The result should be

```
"var": 1,
"longvar": 2,
"verylongvar": 3,
```

### Recording
* To record a macro, in register w, do `qw` in normal mode
    * You can use any letter from a to z to store macros
* To use the recorded macro (stored in register w) do, `@w`. To use it 10 times, do `10@w`
* To apply to all visually selected lines, select the lines and do `'<,'> norm @a`

### Tips
* Use motions such as `w`, `b`, `^`, etc and not `hjkl` if lines are not the same length
