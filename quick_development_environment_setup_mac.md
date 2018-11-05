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

## Sublime Text 3 Configuration
1. Install Package Control
2. Install GitGutter
3. Install SideBarEnhancements
4. Install SublimeLinter (does not include linter)
	- Install SublimeLinter-pycodestyle (also in package control)
5. Install MarkdownPreview
6. Install PEP8 Autoformat
7. Install TrailingSpaces (highlight and remove trailing spaces)
8. Install Git ([this one](https://github.com/kemayo/sublime-text-git))
9. Create a symbolic link from Sublime Text CLI to /usr/local/bin/sub
	* `ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl`
10. Install [Origami](https://github.com/SublimeText/Origami): Create, destroy, zoom into panes using keyboard shortcuts
11. Install [AceJump](https://github.com/ice9js/ace-jump-sublime): Move cursor to any character on screen

### Things to add to user preferences
* Put these in the `Preferences.sublime-settings--User` file found in Preferences > Settings (or by pressing Command + ,)
```json
{
	"font_size": 14,
	"ignored_packages":
	[
	],
	"translate_tabs_to_spaces": true
}
```

## Useful, but not necessary
1. [__Install Honer__](https://github.com/puffnfresh/Honer.app)

## A few useful things to add to .bash_profile
```bash
# added by Anaconda3 installer
export PATH="/anaconda3/bin:$PATH"

# customize prompt with nice colors
# discussion of colors: https://www.howtogeek.com/307701/how-to-customize-and-colorize-your-bash-prompt/
# Color tag comes in the form of \[\033[COLORm\], where COLOR is a number
# for the color of the foreground text (e.g. 30==Black, 36==Cyan)
export PS1='\t \[\033[1;32m\]\W:\[\033[1;34m\]'
# export PS1='\t \[\033[32m\]\W\[\033[30m\]☆'  # alternative
export CLICOLOR=1
export LSCOLORS=Fxfxcxdxbxegedabagacad
export HISTCONTROL=ignoreboth:erasedups  # no duplicates in history

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
## Useful Command Line Tools
1. `man` replacement: [tldr](https://tldr.sh/#installation)
2. `find` replacement: [fd](https://github.com/sharkdp/fd/)
3. `cat` replacement: [bat](https://github.com/sharkdp/bat)
4. `fzf` for quick fuzzy searching: [fzf](https://github.com/junegunn/fzf)
5. Others: https://remysharp.com/2018/08/23/cli-improved

## Miscellaneous settings
* Prevent switching deskstop spaces when switching to an application
	- Go to System Preferences > Mission Control, deselect "When switching to an application, switch to a Space with open windows for the application"


