# Mission 3 — Understand the operating system

## 1. Task / objective

Explore the operating system environment, running processes, storage, paths, file permissions, and describe the OS's key responsibilities.

## 2. Work completed

Gathered system information using terminal commands, observed running processes, explained absolute vs relative paths, examined file permissions, and completed the OS responsibilities table.

## 3. Commands / tools used

`uname -a`, `whoami`, `df -h`, `top` (briefly), `ps aux`, `ls -l`, `pwd`, `cd`

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
|---------------------|-------------------|-------------------------------|
| Operating system / system details | The OS name, version and kernel | Running macOS with a Darwin kernel — this is the Unix-based system that manages all hardware and software on my Mac |
| Current account identity | The username of the currently logged-in user | `whoami` returned my username, confirming which account is active and whose permissions apply to file operations |
| Available and used storage | How much disk space is free and used | `df -h` showed total disk capacity, used space and available space in human-readable units (GB). A good amount of space remained available |
| System activity snapshot | A live view of CPU and memory usage by running programs | `top` briefly showed dozens of active processes with their CPU and memory percentages. The system was mostly idle with a few apps consuming noticeable resources |

### Task 3.2 — Understand processes

- **What is a process?** A process is a running instance of a program. When you open an application, the OS creates a process for it and allocates it CPU time and memory.
- **What does the PID column represent?** PID stands for Process Identifier. It is a unique number the OS assigns to each process so it can track, manage and terminate individual processes.
- **Two example processes:**
  1. A web browser process (e.g. Chrome) — it appears as one or more processes handling tabs and extensions.
  2. A background system process like `WindowServer` on macOS — it manages the graphical display even when no user application is in the foreground.

### Task 3.3 — Understand paths and permissions

- **Absolute path:** A full path starting from the root of the file system, e.g. `/Users/[redacted]/digital-detective-XXXX/mission-03-operating-system`.
- **Relative path:** A path relative to the current directory, e.g. `../mission-02-terminal` (goes up one level, then into the mission-02 folder).
- **Difference:** An absolute path always works regardless of where you are, while a relative path depends on your current location.

**File permissions observed:**

| Permission | Meaning | Example |
|-----------|---------|---------|
| r — Read | Allows a file's contents to be read | Opening a text file to view it |
| w — Write | Allows a file to be changed | Editing a text file and saving it |
| x — Execute | Allows a file to be run; on a directory, allows access/traversal | Running a script like `python3 hello.py` |

Running `ls -l` on a practice file showed a permission string like `-rw-r--r--`, meaning the owner can read and write, while group and others can only read. No one had execute permission on that file.

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
|-------------------|-----------------|---------|
| Process management | The OS decides which processes get CPU time, starts and stops them, and prevents them from interfering with each other | When I open Chrome and VS Code simultaneously, the OS schedules both so they share the CPU fairly |
| Memory management | The OS allocates RAM to each running process and reclaims it when a process ends, ensuring no process uses another's memory | Opening a large file in an editor — the OS gives that editor enough RAM and frees it when the editor is closed |
| Device management | The OS communicates with hardware through drivers so that applications do not need to know the hardware details | Pressing a key on the keyboard — the OS driver captures the signal and delivers it to the active application |
| File management | The OS organises files into a directory structure, controls access, and manages reading/writing to storage | Saving a document — the OS handles finding free space on the SSD and writing the data |
| User interface / shell | The OS provides a way for users to interact with the computer, either graphically (GUI) or through a terminal (CLI) | Using the Terminal to run commands or the Finder to browse files visually |
| Security and permissions | The OS enforces who can read, write or execute each file and prevents unauthorised access | A regular user cannot delete system files because the OS restricts those permissions to the administrator |

## 5. Difficulties faced

No major difficulties. Understanding the three-group permission format (`owner-group-others`) took a moment to parse.

## 6. How I resolved them

I broke down the permission string character by character (`rwxr-xr--`) and matched each triplet to owner, group and others.

## 7. Evidence / files

- This README with all tables and explanations.

## 8. Commit details

- **Commit message:** "Document operating system and file management"
- Pushed to GitHub and verified.
