# Mission 0 — Create your GitHub workspace

## 1. Task / objective

Set up a correctly named GitHub repository with the required folder structure and a root README for the Digital Detective assignment.

## 2. Work completed

- Decided on the repository name following the naming rule: `digital-detective-XXXX` (assignment name + last four USN digits).
- Created the local project folder and opened it in Terminal.
- Created all nine mission folders (`mission-00-setup` through `mission-08-final-report`) and an `evidence/` folder.
- Placed an empty `README.md` inside every mission folder.
- Prepared the root `README.md` with the project title, a short description, and a mission index linking to each folder.
- Created a new public repository on GitHub with the same name and pushed the initial structure.

## 3. Commands / tools used

- `mkdir -p digital-detective-XXXX` — created the project folder.
- `mkdir mission-00-setup mission-01-computer-basics ...` — created each mission subfolder.
- `touch README.md` — created empty README files inside each folder.
- `git init` — initialised the local Git repository.
- `git add .` — staged all files.
- `git commit -m "Set up Digital Detective mission structure"` — committed the setup.
- `git remote add origin <URL>` — linked the local repo to GitHub.
- `git push -u origin main` — pushed the initial commit.
- Python 3 and Git were confirmed installed using `python3 --version` and `git --version`.

## 4. My understanding

A repository is a folder tracked by Git that stores every version of your files. Organising it by mission keeps each topic's work separate and easy to find. The root README acts as a table of contents so anyone visiting the repository immediately understands its purpose and structure.

## 5. Difficulties faced

No major difficulties. I double-checked the naming convention to make sure the repository name matched exactly.

## 6. How I resolved them

I re-read the naming rule in the assignment sheet and confirmed the format before creating the repo.

## 7. Evidence / files

- Root `README.md` with mission index.
- All mission folders with placeholder READMEs visible on GitHub.

## 8. Commit details

- **Commit message:** "Set up Digital Detective mission structure"
- Pushed to GitHub and confirmed all folders and files are visible.
