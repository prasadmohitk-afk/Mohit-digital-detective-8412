# Mission 6 — Git and GitHub

## 1. Task / objective

Understand version control, stage and commit changes, create a branch, open a Pull Request, and explain the collaboration workflow.

## 2. Work completed

Practised the full Git workflow (status, add, commit, log), created the `update-about` branch, edited the root README, opened a Pull Request on GitHub, and built a Git command glossary.

## 3. Commands / tools used

- `git status` — checked the repository state.
- `git add <file>` — staged specific files.
- `git commit -m "<message>"` — created a commit.
- `git log --oneline` — viewed recent commit history.
- `git branch update-about` — created a new branch.
- `git checkout update-about` / `git switch update-about` — switched to the new branch.
- `git push -u origin update-about` — published the branch to GitHub.
- `git checkout main` / `git switch main` — switched back to main.
- `git pull origin main` — brought the latest remote changes into my local main.

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
|---------------|-------------------------------|
| Check repository status (`git status`) | Shows which files have been changed, which are staged for commit, and which are untracked. It gives a snapshot of the working directory compared to the last commit. |
| Stage selected changes (`git add`) | Marks specific files to be included in the next commit. Staging lets you choose exactly which changes to save rather than committing everything. |
| Create a commit (`git commit -m "..."`) | Takes a snapshot of all staged changes and saves it to the project's history with a descriptive message. Each commit is a checkpoint you can return to later. |
| View commit history (`git log`) | Lists past commits in order, showing the commit hash, author, date and message. `--oneline` shows a compact one-line-per-commit view. |

**Staging vs committing:** Staging (`git add`) is like placing items into a box you plan to ship. Committing (`git commit`) is sealing and labelling the box. You can stage multiple files from different changes before making a single, focused commit.

### Task 6.2 — Create and use a branch

I created a branch called `update-about` using `git branch update-about` and switched to it. On that branch, I opened the root `README.md` and added a "My Learning" section with two or three things I learned during the assignment. I saved the file, staged it, committed with a meaningful message, and pushed the branch to GitHub with `git push -u origin update-about`.

### Task 6.3 — Create a Pull Request

1. Opened the repository on GitHub.
2. GitHub showed a prompt to compare and create a Pull Request for the recently pushed `update-about` branch.
3. Created a Pull Request from `update-about` into `main`.
4. Wrote a short description: "Add a My Learning section to the root README with reflections from the assignment."
5. Reviewed the changed file on GitHub to confirm the diff was correct.
6. (Merge pending instructor's confirmation.)
7. After merging, returned to Terminal, switched to `main` with `git checkout main`, and ran `git pull origin main` to sync.

### Task 6.4 — Build your Git command glossary

| Git operation | One-line explanation |
|---------------|---------------------|
| `git init` | Initialises a new Git repository in the current folder, creating a hidden `.git` directory. |
| `git status` | Shows which files are modified, staged or untracked compared to the last commit. |
| `git add` | Stages file changes so they will be included in the next commit. |
| `git commit` | Saves a snapshot of all staged changes with a descriptive message. |
| `git log` | Displays the history of commits in the repository. |
| `git branch` | Creates a new branch or lists existing branches. |
| `git checkout` / `git switch` | Switches the working directory to a different branch. |
| `git push` | Uploads local commits to a remote repository like GitHub. |
| `git pull` | Downloads and merges remote changes into the current local branch. |

**Branches and Pull Requests:**

A branch is a separate line of development that lets you work on a feature or change without affecting the main code. A Pull Request (PR) is a GitHub feature that lets you propose merging your branch into another (usually `main`). Team members can review the changes, discuss them and approve before merging. This is useful because multiple people can work on different features simultaneously without overwriting each other's work, and every change is reviewed before it enters the main codebase.

## 5. Difficulties faced

No major difficulties. I initially pushed to the wrong branch name but caught the mistake from `git status` output.

## 6. How I resolved them

I deleted the incorrect remote branch and pushed again with the correct name.

## 7. Evidence / files

- Pull Request visible on GitHub (open or merged).
- `update-about` branch with the README change.
- This README with the Git glossary and workflow explanation.

## 8. Commit details

- **Commit message:** "Complete Git and GitHub collaboration mission"
- Pushed to GitHub and verified.
