# Basic Git and GitHub Workflow

## Definitions
* `HEAD`: latest commit on the current branch. To see where HEAD is pointing to, do `cat .git/HEAD`. Defined only for local branches in local repository.
* `working tree`: "files that you are currently working on."([source](https://stackoverflow.com/a/29625893)), the same as `HEAD` upon checkout


## Setting Up a Repository

1. Create a folder that will contain the codes you will version control
	- For example, call it project_x

2. Create a repository with the same name on GitHub

3. Execute the following commands in Terminal

        echo "# Project X" >> README.md
        git init
        git add README.md
        git commit -m "first commit"
        git remote add origin git@github.com:palpen/project_x.git
        git push -u origin master

The repository is now ready and you can begin saving your code in it and, subsequently, committing changes and pushing them to GitHub.


## Adding, Committing, and Pushing Changes

Suppose you've made changes to the python script, x_code.py. To push the change you made to GitHub, you must

1. stage the change by executing

        git add x_code.py

2. then , if this is the only change you'd like staged for this commit, execute

	    git commit -m "small minor update"

3. Now back everything up in GitHub by executing

	    git push

In part 3, you may need to instead execute

    git push origin master

if you are not on the master branch.


## How to Clone a Repository

Get the SSH url of the repository you want to clone from the repository's GitHub page. The SSH url for this repository, for example, is

    git@github.com:palpen/git_workflow.git

Then

    git clone git@github.com:palpen/git_workflow.git

will save a copy of this repository to the current directory. You can then begin editing the cloned repository and update the master copy by adding, committing, and pushing the changes to GitHub (following the instructions above).


## Create a new branch, work in it, and merge to master when ready

To create and checkout a new branch, execute

```
git checkout -b new_branch_name
```

When you are ready to merge the changes you've made in `new_branch_name` to the master branch, add and commit your changes and execute the following commands

```
git checkout master
git pull origin master
git merge new_branch_name
```

You can then push to the remote repository when ready:

```
git push origin master
```

Reference:
1. https://stackoverflow.com/questions/5601931/best-and-safest-way-to-merge-a-git-branch-into-master

## Moving uncommitted changes to new branch
You're editing your code and would like to create a new branch for the changes you've made and, subsequently, commit and add these changes to this new branch (perhaps you're not confident that the changes you've made works well enough to be a part of the master branch yet).

* create a new branch with current uncommitted changes

        git checkout -b <new-branch-name>

* add files you want in this new branch

        git add <files>

* commit these files to the new branch

        git commit -m "<Brief description of this commit>"

To return to the master branch from the new branch:

    git checkout master

Similarly, from the master branch, you can switch to your newly created branch using the same command above:

    git checkout <branch-name>

## Various ways to `git diff`
__Examples below draw from EXAMPLES section of `git diff --help`__

Checking your working tree
`git diff`: compare index with working tree
`git diff --cached`: compare staged (index) with most recent commit (HEAD)
`git diff HEAD`: compare most recent commit (HEAD) with all changes (shows difference between working tree or index and HEAD); what you would be committing if you run "git commit -a"

Comparing with arbitrary commits
`git diff test`: instead of using the tip of the current branch, compare with the tip of "test" branch
`git diff HEAD -- ./test.txt`: compare most recent commit (HEAD) with any changes in test.txt
`git diff HEAD^ HEAD`: compare the version before the last commit and the last commit

Comparing branches
`git diff topic master`: compare between the tips of the topic and the master branches
`git diff topic..master`: same as above
`git diff topic...master`: changes that occurred on the master branch since when the topic branch was started off it.

## Check if there is merge conflict between two branches
[source](https://stackoverflow.com/a/10879368)
Suppose you want to check if there are merge conflicts betwen `dev` and `master`. In `master` branch, do:
    `git merge dev --no-ff --no-commit`


## Credential Caching

You've cloned a repository using a url beginning with HTTPS (e.g. https://github.com/username/reponame.git). Every time you push to the remote repository it asks you for your username and password. To avoid this, enable credential caching for the repository by executing the following commands in the terminal

```
git config --global credential.helper store
git config --global credential.helper 'cache --timeout 7200'
```

The default password cache timeout is 15 minutes. The last line changes this to 2 hours.

References:
1. https://stackoverflow.com/questions/6565357/git-push-requires-username-and-password
2. https://help.github.com/articles/caching-your-github-password-in-git/#platform-linux

## Other Things to Include

1. Checking out a commit
2. Commands to quickly revert back to the most recent commit
