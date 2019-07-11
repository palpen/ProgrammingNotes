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

## Search and replace
* Place a # in front of every line: `:%s/^/#/`
* Place a , at the end of every line: `:%s/$/,/`

## Commands
* Insert blank line below cursor (in command mode): `control + o`
    * Not really a vim command but works in Sublime Text using NeoVintageous
* How to comment / uncomment out a block of code: https://stackoverflow.com/a/23063140/3649966

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
set softtabstop=4
set ruler
set undolevels=1000
set backspace=indent,eol,start
syntax on
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
