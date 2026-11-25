# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Use the command-line interface to inspect folders, create and manage practice files, understand flags and pipes, and explain package managers.

## 2. Work completed

Practised all basic terminal operations, performed safe file changes, explored flags and pipes, and looked into Homebrew as a package manager.

## 3. Commands / tools used

`pwd`, `ls`, `ls -la`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `echo`, `head`, pipe (`|`)

## 4. My understanding

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
|--------------------------|-------------|-----------------|
| Current-directory display (`pwd`) | Prints the full path of the folder I am currently inside | It showed the absolute path to my project folder, confirming my location in the file system |
| Directory listing (`ls`) | Lists the names of files and folders in the current directory | I saw all my mission folders and the root README listed |
| Detailed listing (`ls -la`) | Lists files with extra details: permissions, owner, size, modification date, and hidden files | I noticed hidden files like `.git` appeared, and each entry showed its permission string (e.g. `drwxr-xr-x`) |
| Change directory (`cd ..`) | Moves into a different folder; `cd ..` goes up one level to the parent | My prompt and `pwd` output changed to the parent folder's path |
| Create directory (`mkdir practice`) | Creates a new empty folder with the given name | A folder called `practice` appeared in my listing |
| Create empty file (`touch notes.txt`) | Creates a new empty file, or updates the timestamp if it already exists | An empty `notes.txt` appeared inside the practice folder |
| Copy file (`cp notes.txt notes_backup.txt`) | Makes a duplicate of a file with a new name | Both `notes.txt` and `notes_backup.txt` existed with the same content |
| Move / rename file (`mv notes_backup.txt notes_copy.txt`) | Renames or moves a file to a new name or location | The file `notes_backup.txt` disappeared and `notes_copy.txt` appeared |
| Display file contents (`cat notes.txt`) | Prints the entire contents of a file to the terminal | The text I had added to the file was displayed |

### Task 2.2 — Practise file changes safely

I created a folder `terminal-practice` inside the repository, created a file `practice.txt`, added one line using `echo "First line" > practice.txt`, then appended a second line using `echo "Second line" >> practice.txt`. Running `cat practice.txt` showed both lines. I made a backup with `cp practice.txt practice_backup.txt` and renamed it with `mv practice_backup.txt practice_renamed.txt`.

**Answers:**

- **Replacing vs appending:** Using `>` replaces the entire file content with new text. Using `>>` appends text to the end without removing what was already there.
- **Copying vs moving:** Copying (`cp`) creates a duplicate — both the original and the copy exist. Moving (`mv`) relocates or renames the file — the original name or location no longer exists.
- **Current-directory display:** `pwd` tells you exactly where you are in the folder hierarchy, which prevents accidentally creating files in the wrong place.
- **Why directory listing is useful:** `ls` lets you see what files and folders exist before running commands, so you can verify names and avoid mistakes.

### Task 2.3 — Understand flags and pipes

- Running `ls` shows file names only. Running `ls -la` adds permissions, hidden files and human-readable sizes (`ls -lah`). The flags change the detail level of the output.
- **Pipe example:** `ls -la | head -5` — the pipe (`|`) takes the output of `ls -la` and sends it as input to `head -5`, which displays only the first five lines. The left side produces data, the pipe connects them, and the right side filters or processes that data.

### Task 2.4 — Understand package managers

Homebrew is a package manager for macOS. It simplifies installing, updating and removing software through simple terminal commands like `brew install <package>`. Package managers are useful because they handle downloading the correct version, resolving dependencies, and keeping software up to date — all without needing to visit websites or manually manage files. Without a package manager, you would need to find each tool's website, download the right version for your system, and manually update it later.

## 5. Difficulties faced

No major difficulties. I initially forgot the difference between `>` and `>>` and accidentally replaced a file's content instead of appending.

## 6. How I resolved them

I re-created the file and remembered that `>` overwrites while `>>` appends. This reinforced the importance of choosing the right redirect operator.

## 7. Evidence / files

- `terminal-practice/` folder with practice files created during the mission.
- This README with completed tables and explanations.

## 8. Commit details

- **Commit message:** "Complete Terminal and file management mission"
- Pushed to GitHub and verified.
