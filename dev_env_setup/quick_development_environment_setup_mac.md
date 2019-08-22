# Quick Development Environment Setup on Mac

## Can't live without
1. [SublimeText](https://www.sublimetext.com/): Text editor
	- Add `alias subl='open -a "/Applications/Sublime Text.app" '` to start-up script
2. [Iterm2](https://www.iterm2.com/): Better terminal emulator than Terminal
	- Enable command line key navigation using Alt (Option) button:
		- In Iterm, hit Command + O, to open profiles. Click `Edit Profiles…` and under the `Keys` tab, select `Esc+` for both Left and Right Option key (Source: https://stackoverflow.com/questions/18923765/bash-keyboard-shortcuts-in-iterm-like-altd-and-altf)
	- See `iterm2_profile` folder for custom settings
		- See http://stratus3d.com/blog/2015/02/28/sync-iterm2-profile-with-dotfiles-repository/
	- Install and set up __Oh-My-Zsh__
3. [Miniconda](https://docs.conda.io/en/latest/miniconda.html): Lightweight version of [Anaconda](https://www.anaconda.com/distribution/)
    - Move conda initializer from `.bash_profile` to `.zshrc`
4. [Spectacle](https://www.spectacleapp.com/): Window manager
5. [XCode](https://developer.apple.com/xcode/): MacOS developer tools 
	- `xcode-select --install`
6. [Homebrew](https://brew.sh/): Package manager for MacOS
7. Google Chrome with Vimium Extension

## If Necessary
1. Docker
2. Dropbox
3. 1Password

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
12. Install [ayu](https://github.com/dempfi/ayu): Very nice and modern theme
13. Install [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous): Vim emulator

### Set-up to allow remote editing using Sublime Text 3
Install [RemoteSubl](https://github.com/randy3k/RemoteSubl) and follow all instructions in the README. In particular
* `mv /usr/local/bin/rmate /usr/local/bin/rsubl` to give command a more intuitive name
* Add to SSH config in `~/.ssh/config`
	```
	Host myremote
		HostName HOSTNAME
		RemoteForward 52698 localhost:52698
		User USERNAME
	```
	so that connection is as simple as `ssh myremote`

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


