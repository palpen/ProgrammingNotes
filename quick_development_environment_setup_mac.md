# Quick Development Environment Setup on Mac


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
3. __Install Anaconda__
	- After installation, make sure that `export PATH="/anaconda3/bin:$PATH"` is in .bash_profile
	- Then `source .bash_profile`
	- To check, `which python` (`which` locates program file within user’s path) and should see `/anaconda3/bin/python`
4. __Install Spectacle (Organize windows using shortcuts)__
5. __Install XCode (includes important developer tools, like git)__

## If Necessary

1. __Install Docker__
