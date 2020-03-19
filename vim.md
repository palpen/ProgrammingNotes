# Notes on Vim

I use [Sublime Text 3](https://www.sublimetext.com) with the [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) plugin to use Vim key bindings.

For basic vim motions and commands, type `vimtutor` in your command line if you are in a Unix environment.

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

## Delete, yank and put
D -> delete from cursor to end of line (characterwise)

### Inserting a line in the middle of another line
`dd` will do a linewise deletion, which following a put command, `P` or `p`, will either insert the deleted line before or after the line in which the cursor is located. To insert the deleted line at the cursor position, do a characterwise deletion, `0D` (0 will move cursor to the begining of the line and `D` will do a characerwise deletion from the cursor to the end of the line). See https://vimhelp.org/motion.txt.html#linewise

## Buffers
vims way of editing multiple files within the same vim session.

* To open a file in the same vim session, do `:e <FILENAME>`
* To list files in the buffer, do `:ls`
* To toggle across files in the buffer, do `:b <TAB>`
    * One can also type name of the file in the buffer or its number
    * `:b myfile.py` or `:b 2`
* To toggle / switch between current and previous buffer, do `Control + 6`

## Search and replace
* Place a # in front of every line: `:%s/^/#/`
* Place a , at the end of every line: `:%s/$/,/`

## Commands and shortcuts
* Insert blank line below cursor (in command mode): `control + o`
    * Not really a vim command but works in Sublime Text using NeoVintageous
* How to comment / uncomment out a block of code: https://stackoverflow.com/a/23063140/3649966
* Copy to clipboard
    * Visually select segment to copy, then `:w !pbcopy`
* Display name of current file: Control + g
* Search for word under cursor (in vim): place cursor on word then press, * (Shift + 8)
* Delete character across selected group spanning multiple lines
    * https://stackoverflow.com/a/48952069/3649966
    * Use visual-block to highlight lines, then ":", then "%normal $x", then hit enter

## Configuring VimR
* [VimR](http://vimr.org) is a GUI based text editor build on NeoVim.
* To configure the editor created an `init.vim` file in `~/.config/nvim`. Use `init.vim` the same way you would use a `.vimrc` file.
* Color themes are stored in `~/.config/nvim/colors`
	* Here's a useful color scheme [NeoSolarized](https://github.com/icymind/NeoSolarized)

## Basic .vimrc
```
set number
set linebreak
set showbreak=+++
set textwidth=100
set showmatch
set visualbell
set hlsearch
set smartcase
set ignorecase
set incsearch
set autoindent
set smartindent
set smarttab
set expandtab
set paste
set statusline=2
set statusline=%f
set softtabstop=0 noexpandtab
set shiftwidth=4
set tabstop=4
set ruler
set undolevels=1000
set backspace=indent,eol,start
set belloff=all
color desert
syntax on


" <Ctrl-l> redraws the screen and removes any search highlighting.
nnoremap <silent> <C-l> :nohl<CR><C-l>
" Highlight trailing whitespace
highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/

fun! TrimWhitespace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
endfun
```

## Preview markdown files
* Install the Google Chrome browser
* Install the MarkDown Preview Plus Extension on Chrome (follow usage instructions)
    * Chrome > Preferences > Markdown Preview Plus > Enable `Allow access to file URLs`
* in Vim, open markdow file by `:!open -a /Applications/Google\ Chrome.app mymarkdownfile.md`

## Basic Vim Setup on Remote Server

___tmux + vim + gruvbox color scheme___
* Install Pathogen (vim plugin manager): https://github.com/tpope/vim-pathogen
    * Add `execute pathogen#infect()` to top .vimrc config file
* Place `export TERM=xterm-256color` in .bashrc or .zshrc config file
* Install gruvbox colorscheme using Pathogen: https://github.com/morhetz/gruvbox/wiki/Installation
* In .vimrc config file, add the following
    * `syntax on`
    * `colorscheme gruvbox`
    * `set background=dark`
