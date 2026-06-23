# Git Notes — Interview Review

Status: **~95% done** (G1–G7). Answer in 3 beats.

## The three areas
Working Directory → (`git add`) → Staging Area → (`git commit`) → Repository (`git push` → remote)

## Core cycle
- edit files
- `git status` : what changed / what's staged
- `git diff`   : unstaged changes (working dir vs staging); `git diff --staged` for staged
- `git add`    : stage changes
- `git commit` : snapshot staged changes

## Branching
- `git branch <name>` create, `git checkout -b <name>` create+switch, `git switch <name>` switch.
- A branch is just a movable pointer to a commit.

## Merge vs rebase
- **Merge:** combines branches with a new **merge commit** (two parents). Preserves true history, makes a diamond.
- **Rebase:** replays your commits on top of another branch → **linear** history, **new hashes** (rewrites history).
- **Golden rule:** never rebase commits you've already pushed/shared. (Misconception fixed: rebase does NOT squash to one commit.)

## Undoing: reset vs revert
- **`git revert <c>`:** creates a new commit that inverts `<c>`. Safe on shared history.
- **`git reset <c>`:** moves the branch pointer back. Modes:
  - `--soft` keep changes staged
  - `--mixed` (default) keep changes unstaged
  - `--hard` discard changes (destructive)

## Fetch vs pull
- **`git fetch`:** downloads remote commits only (safe, doesn't touch working tree).
- **`git pull`:** fetch + merge into current branch.
- **Ahead** of remote → push. **Behind** → pull.

## HEAD
- `HEAD` → current branch → current commit.
- **Detached HEAD** = HEAD points straight at a commit (not a branch). Commits made here can be lost if you switch away without a branch.

## Merge conflicts
- Git marks conflicts with `<<<<<<<`, `=======`, `>>>>>>>`. Edit to resolve → `git add` → `git commit`.
- Bail out with `git merge --abort`.

## Handy (overview, revisit if needed)
- `git stash` / `git stash pop` — shelve uncommitted work.
- `git cherry-pick <c>` — apply one commit onto current branch.
- `git reflog` — history of where HEAD has been (recover "lost" commits).
- `git tag <name>` — mark a release point.
