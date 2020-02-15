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
set shiftwidth=4
set smartindent
set smarttab
set statusline=2
set statusline=%f
set softtabstop=4
set ruler
set undolevels=1000
set backspace=indent,eol,start
set belloff=all
color desert
syntax on

" <Ctrl-l> redraws the screen and removes any search highlighting.
nnoremap <silent> <C-l> :nohl<CR><C-l>
```

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
