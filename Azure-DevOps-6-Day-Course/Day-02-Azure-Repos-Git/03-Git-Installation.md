# 03 - Git Installation

## Overview

Before you can use Git, you need to install it and set your identity. This lesson covers installation on Windows, macOS, and Linux, plus the essential first-time configuration.

## Installing Git

### Windows
1. Download from [git-scm.com/download/win](https://git-scm.com/download/win).
2. Run the installer. Accept defaults; notable options:
   - Default editor (VS Code is a good choice).
   - "Git from the command line and also from 3rd-party software".
3. This also installs **Git Bash**, a Unix-like shell.

Alternatively, with [winget](https://learn.microsoft.com/windows/package-manager/):
```powershell
winget install --id Git.Git -e
```

### macOS
Easiest with [Homebrew](https://brew.sh):
```bash
brew install git
```
Or install Apple's command line tools:
```bash
xcode-select --install
```

### Linux
```bash
# Debian / Ubuntu
sudo apt update && sudo apt install git -y

# Fedora
sudo dnf install git -y

# Arch
sudo pacman -S git
```

## Verify the Installation

```bash
git --version
# e.g., git version 2.45.0
```

## First-Time Configuration

Set your identity — these appear on every commit you make:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Set a default branch name and a default editor:

```bash
git config --global init.defaultBranch main
git config --global core.editor "code --wait"   # VS Code
```

Helpful quality-of-life settings:

```bash
# Better, colored output
git config --global color.ui auto

# Handle line endings (Windows)
git config --global core.autocrlf true
# Handle line endings (macOS/Linux)
git config --global core.autocrlf input
```

View your configuration:

```bash
git config --list
git config user.name
```

Configuration is stored in:
- **System:** `/etc/gitconfig` (all users)
- **Global:** `~/.gitconfig` (your user)
- **Local:** `.git/config` (the current repo)

Local overrides global, which overrides system.

## Authentication to Azure Repos

When you push/clone from Azure Repos you'll authenticate. Options:

1. **Git Credential Manager (GCM)** — installed with Git for Windows; handles OAuth automatically (recommended).
2. **Personal Access Token (PAT)** — generate from **User settings → Personal access tokens** and use it as the password.
3. **SSH keys** — add a public key under **User settings → SSH public keys**.

> For most users, Git Credential Manager "just works" with a browser sign-in.

## Optional: Configure a GUI / IDE

- **VS Code** has excellent built-in Git support.
- **Visual Studio** integrates with Azure Repos directly.
- GUI clients: GitKraken, Sourcetree, GitHub Desktop.

## Summary

- Install Git for your OS and verify with `git --version`.
- Always set `user.name` and `user.email` globally.
- Authenticate to Azure Repos via Git Credential Manager, a PAT, or SSH.

## Knowledge Check

1. Which two `git config` settings should you always set first?
2. What is the difference between `--global` and `--local` config?
3. Name two ways to authenticate to Azure Repos.

➡️ Next: [04 - Git Basic Commands](./04-Git-Basic-Commands.md)
