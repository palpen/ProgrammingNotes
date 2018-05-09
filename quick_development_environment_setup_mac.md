# Quick Development Environment Setup on Mac


1. Install SublimeText
	- !!! Sync package set up with one at home
	- Add alias to bash profile to open Sublime Text in command line
		- `alias sub='open -a "/Applications/Sublime Text.app" '`
2. Install Iterm2 (version 3)
	- How to enable command line key navigation using the Alt (Option):
		- In Iterm, hit Command + O, to open profiles. Click `Edit Profiles…` and under the `Keys` tab, select `Esc+` for both Left and Right Option key
		- Source: https://stackoverflow.com/questions/18923765/bash-keyboard-shortcuts-in-iterm-like-altd-and-altf
	- !!! Sync bash aliases
3. Install Anaconda
	- After installation, make sure that `export PATH="/anaconda3/bin:$PATH"` is in .bash_profile
	- Then `source .bash_profile`
	- To check, `which python` (`which` locates program file within user’s path) and should see `/anaconda3/bin/python`
4. Install Spectacle (Organize windows using shortcuts)
5. Install XCode (includes important developer tools, like git)

## If Necessary

1. Install Docker