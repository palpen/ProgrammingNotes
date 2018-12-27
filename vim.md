# Notes on Vim

I use [Sublime Text 3](https://www.sublimetext.com) with the [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) plugin to use Vim key bindings.

For basic vim motions and commands, type `vimtutor` in your command line if you are in a Unix environment.

## Motion
Reference: (Text-object selection)[http://vimdoc.sourceforge.net/htmldoc/motion.html#object-select]
* Select a word: `viw`
* Select contents inside braces: `vib`
* Select contents inside quotes: `vi<QUOTE CHARACTER>`
    * `vi"`
* Move cursor to previous or next empty line: `}` or `{`

## Commands
* Insert blank line below cursor (in command mode): `control + o`
    * Not really a vim command but works in Sublime Text using NeoVintageous

## Configuring VimR
* [VimR](http://vimr.org) is a GUI based text editor build on NeoVim.
* To configure the editor created an `init.vim` file in `~/.config/nvim`. Use `init.vim` the same way you would use a `.vimrc` file.
* Color themes are stored in `~/.config/nvim/colors`
	* Here's a useful color scheme [NeoSolarized](https://github.com/icymind/NeoSolarized)
