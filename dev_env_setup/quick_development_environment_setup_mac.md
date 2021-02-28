# Development Environment Setup on Mac

## Must Have

1. [XCode](https://developer.apple.com/xcode/): MacOS developer tools
	- `xcode-select --install`
2. [Homebrew](https://brew.sh/): Package manager for MacOS
3. [Alacritty](https://github.com/alacritty/alacritty): terminal emulator
4. [Oh-My-Zsh](https://ohmyz.sh/): Zsh shell and its framework
5. [Miniconda](https://docs.conda.io/en/latest/miniconda.html): Lightweight version of [Anaconda](https://www.anaconda.com/distribution/)
    - Move conda initializer from `.bash_profile` to `.zshrc`
6. [Rectangle](https://github.com/rxhanson/Rectangle): Window manager
7. Google Chrome

## If Necessary
1. Docker
2. Dropbox
3. 1Password

## Useful, but not too important
1. [zshmarks](https://github.com/jocelynmallon/zshmarks): Commandline directory bookmarking
2. [trash-cli](http://hasseg.org/trash/): Avoid `rm -rf *` horror and move deleted files to trash instead (can be installed with `brew install trash`)

## Useful settings and aliases to add to .zshrc
```bash
# Remove duplicates in history
setopt HIST_IGNORE_ALL_DUPS
alias jn='jupyter notebook'
alias zzz='pmset sleepnow'

# git
alias lgrh='echo "List GitHub clone url";curl https://api.github.com/users/palpen/repos?per_page=100 | grep  -o "https://github.com/[^\"]*\.git"'
alias ga='git add '
alias gc='git commit -m '
alias gst='git status'
```

## Vim and Tmux config files
See https://github.com/palpen/config_files

## Miscellaneous settings
* Prevent switching deskstop spaces when switching to an application
	- Go to System Preferences > Mission Control, deselect "When switching to an application, switch to a Space with open windows for the application"

