# Quick Development Environment Setup on Mac

## Can't live without
1. __Install SublimeText__
	- !!! Sync package set up with one at home
	- Add alias to bash profile to open Sublime Text in command line
		- `alias sub='open -a "/Applications/Sublime Text.app" '`
2. __Install Iterm2 (version 3)__
	- How to enable command line key navigation using the Alt (Option):
		- In Iterm, hit Command + O, to open profiles. Click `Edit Profiles…` and under the `Keys` tab, select `Esc+` for both Left and Right Option key
		- Source: https://stackoverflow.com/questions/18923765/bash-keyboard-shortcuts-in-iterm-like-altd-and-altf
	- !!! Sync bash aliases
	- Set color to `Solarized Dark` (Profiles > Open Profiles > Default > Edit Profiles...> Colors tab > Color Presets... pull down)
	- Customize prompt with nice colors (see below)
	3. __Install Anaconda__
	- After installation, make sure that `export PATH="/anaconda3/bin:$PATH"` is in .bash_profile
	- Then `source .bash_profile`
	- To check, `which python` (`which` locates program file within user’s path) and should see `/anaconda3/bin/python`
4. __Install Spectacle (Organize windows using shortcuts)__
5. __Install XCode (includes important developer tools, like git)__
6. __Install Google Chrome__
	* Install Vimium

## If Necessary
1. __Install Docker__
2. __Install Dropbox__

## Useful, but not necessary
1. [__Install Honer__](https://github.com/puffnfresh/Honer.app)

## Sublime Text 3 Configuration
1. __Install Package Control__
2. __Install GitGutter__
3. __Install SideBarEnhancements__
4. __Install SublimeLinter__ (does not include linter)
	- Install SublimeLinter-pycodestyle (also in package control)
5. __Install MarkdownPreview__
6. __Install PEP8 Autoformat__
7. __Install TrailingSpaces__ (highlight and remove trailing spaces)
8. __Install Git__ ([this one](https://github.com/kemayo/sublime-text-git))

## A few useful things to add to .bash_profile
```bash
# added by Anaconda3 installer
export PATH="/anaconda3/bin:$PATH"

# customize prompt with nice colors
export PS1="\W|☃︎ "
export CLICOLOR=1
export LSCOLORS="gxfxcxdxBxegecabagacad"

# Use fzf copy directory path to clipboard
# usage: cdf -> search directory or filename -> enter to copy directory to clipboard
# tr -d '\n' before pbcopy removes next line character to avoid auto execution
# in command line
cdf() {
   local file
   local dir
   file=$(fzf +m -q "$1") && dir=$(dirname "$file") && echo "$dir" | tr -d '\n' | pbcopy
}

alias sub='open -a "/Applications/Sublime Text.app" '
alias zzz='pmset sleepnow'
```


