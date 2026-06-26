# Git Cheat Sheet

A concise reference of the Git commands you will use throughout this course.

---

## Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --list                       # view all settings
```

## Creating / Cloning Repositories

```bash
git init                                # create a new repo in current dir
git clone <url>                         # clone a remote repo
git clone <url> myfolder                # clone into a specific folder
```

## Everyday Workflow

```bash
git status                              # show changed files
git add <file>                          # stage a file
git add .                               # stage everything
git commit -m "message"                 # commit staged changes
git commit -am "message"                # stage tracked files + commit
git log --oneline --graph --all         # compact history graph
git diff                                # unstaged changes
git diff --staged                       # staged changes
```

## Branching

```bash
git branch                              # list local branches
git branch <name>                       # create a branch
git checkout <name>                     # switch branches
git checkout -b <name>                  # create + switch
git switch <name>                       # modern switch
git switch -c <name>                    # create + switch (modern)
git merge <branch>                      # merge branch into current
git branch -d <name>                    # delete a merged branch
git branch -D <name>                    # force-delete a branch
```

## Working with Remotes

```bash
git remote -v                           # list remotes
git remote add origin <url>             # add a remote
git push -u origin main                 # push and set upstream
git push                                # push to upstream
git pull                                # fetch + merge
git fetch                               # download without merging
```

## Undoing Changes

```bash
git restore <file>                      # discard working-dir changes
git restore --staged <file>             # unstage a file
git reset --soft HEAD~1                 # undo last commit, keep changes staged
git reset --hard HEAD~1                 # undo last commit, discard changes (danger)
git revert <commit>                     # create a new commit that undoes a commit
```

## Stashing

```bash
git stash                               # save uncommitted changes
git stash list                          # list stashes
git stash pop                           # reapply and drop latest stash
git stash apply                         # reapply but keep stash
git stash drop                          # delete a stash
```

## Tags

```bash
git tag                                 # list tags
git tag v1.0.0                          # lightweight tag
git tag -a v1.0.0 -m "Release 1.0.0"    # annotated tag
git push origin v1.0.0                  # push a tag
git push origin --tags                  # push all tags
```

## Rebasing

```bash
git rebase main                         # replay current branch onto main
git rebase -i HEAD~3                     # interactive rebase last 3 commits
git rebase --continue                   # continue after resolving conflicts
git rebase --abort                      # cancel a rebase
```

## Inspecting

```bash
git show <commit>                       # show a commit's details
git blame <file>                        # who changed each line
git log --author="name"                 # filter history by author
git log -- <file>                       # history for a specific file
```

## Resolving Merge Conflicts

1. Run the merge/pull; Git marks conflicts in the file:

```
<<<<<<< HEAD
your changes
=======
incoming changes
>>>>>>> branch-name
```

2. Edit the file to keep the correct content and remove the markers.
3. Stage and commit:

```bash
git add <file>
git commit
```

---

## .gitignore Quick Examples

```gitignore
# Node
node_modules/
npm-debug.log

# Python
__pycache__/
*.pyc
.venv/

# .NET
bin/
obj/

# OS / editor
.DS_Store
.vscode/
*.log
```

See the [Azure DevOps Cheat Sheet](./Azure-DevOps-Cheat-Sheet.md) for platform-specific commands.
