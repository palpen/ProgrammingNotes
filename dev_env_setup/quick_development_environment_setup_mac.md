# Development Environment Setup on Mac

## Must Have
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

## Sublime Text 3 Packages
1. [Package Control](https://packagecontrol.io/): Package manager for Sublime Text
2. [AnacondaST3](http://damnwidget.github.io/anaconda/#): Full featured Python IDE for Sublime Text 3
3. [SideBarEnhancement](https://github.com/titoBouzout/SideBarEnhancements)
4. [SublimeLinter](http://www.sublimelinter.com/en/stable/): Linting framework
	- SublimeLinter-pycodestyle: Linter, basically PEP 8 (installed using Package Control)
5. [MarkdownPreview](https://github.com/facelessuser/MarkdownPreview)
6. [PEP8 Autoformat](https://github.com/wistful/SublimeAutoPEP8): Format code according to PEP8
7. [TrailingSpaces](https://github.com/SublimeText/TrailingSpaces): Highlight and remove trailing spaces
8. [Origami](https://github.com/SublimeText/Origami): Create, destroy, zoom into panes using keyboard shortcuts
9. [ayu](https://github.com/dempfi/ayu): Very nice and modern looking theme
10. [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous): Vim emulator
	* Must add the following to Sublime Text preferences to work properly:
	```
	...
	"ignored_packages":
	[
		"Six",
		"Vintage",
		"Vintageous"
	],
	"vintageous_use_ctrl_keys": true,
	...
	```

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
	"translate_tabs_to_spaces": true
}
```

## Useful, but not too important
1. [Honer](https://github.com/puffnfresh/Honer.app): Draws a line around currently active window
2. [zshmarks](https://github.com/jocelynmallon/zshmarks): Commandline directory bookmarking
3. [trash-cli](http://hasseg.org/trash/): Avoid `rm -rf *` horror and move deleted files to trash instead (can be installed with `brew install trash`)

## A few useful things to add to .zshrc
```bash
# Remove duplicates in history
setopt HIST_IGNORE_ALL_DUPS
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

* Restore windows, tabs, and panes when restarting Iterm2
    * In Iterm2 under Preferences > General > Startup set the Window restoration policy to "Use System Window Restoration Setting"
    * In MacOS, go to System Preferences > General and uncheck "Close windows when quitting an app"
