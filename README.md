#  Git Command Reference Guide

A complete cheat sheet for all essential Git commands and workflows, organized for quick reference.

---

##  Setup & Configuration

```bash
# Set your identity (required for commits)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
```bash

# Configure default branch name
git config --global init.defaultBranch main

# Set VS Code as default editor
git config --global core.editor "code --wait"

# View all configurations
git config --list
```

##  Getting Started
```bash
# Initialize new repository
git init                        # Current directory
git init project-name           # Specific directory


```
```bash
# Clone existing repository
git clone https://github.com/user/repo.git
git clone https://url.com/repo.git folder-name  # Into specific folder
```
##  Making Changes
```bash
# Check repository status
git status

# Stage changes
git add file.txt                # Specific file
git add .                       # All files
git add *.js                    # Wildcard pattern

# Commit changes
git commit -m "Commit message"  # Standard commit
git commit -am "Message"        # Add tracked files + commit

# Compare changes
git diff                        # Unstaged changes
git diff --staged               # Staged changes
git diff HEAD~3 HEAD            # Between commits
```
## Branch Management
```bash
# List branches
git branch                      # Local branches
git branch -r                   # Remote branches
git branch -a                   # All branches

# Create branches
git branch feature-x            # Create branch
git checkout -b hotfix          # Create + switch

# Switch branches
git checkout main               # Using checkout
git switch feature-x            # Newer syntax

# Delete branches
git branch -d old-branch        # Safe delete
git branch -D old-branch        # Force delete

# Rename branch
git branch -m new-name          # Current branch
git branch -m old-name new-name # Specific branch
```
## Merging & Rebasing
```bash
# Basic merge
git checkout main
git merge feature-branch

# Squash merge
git merge --squash feature-branch
git commit -m "Squashed feature"

# Rebase current branch
git rebase main

# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# Resolve conflicts
git mergetool                   # Use visual tool
git add .                       # After resolving
git rebase --continue           # Continue rebase
```
## Undoing Changes
```bash
# Amend last commit
git commit --amend -m "New message"

# Unstage file
git restore --staged file.txt

# Discard unstaged changes
git restore file.txt

# Revert a commit
git revert commit-hash

# Reset repository (CAUTION)
git reset --soft HEAD~1         # Undo commit, keep changes
git reset --mixed HEAD~1        # Default: undo commit + unstage
git reset --hard HEAD~1         # Completely remove changes
```
## Reviewing History
```bash
# View commit history
git log                          # Full commit history
git log --oneline                # Compact view
git log --graph --oneline        # Branch visualization

# Show specific commit
git show <commit-hash>

# View file change history
git log file.txt
```
