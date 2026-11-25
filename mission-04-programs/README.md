# Mission 4 — How programs run

## 1. Task / objective

Run a simple Python program and compare how compilers and interpreters translate or execute programs.

## 2. Work completed

Created `hello.py`, ran it with Python 3, and completed the compiler vs interpreter comparison table.

## 3. Commands / tools used

- `python3 hello.py` — ran the Python file from Terminal.
- A text editor to write the program.

## 4. My understanding

### Task 4.1 — Create and run a Python program

I created a file called `hello.py` inside this mission folder containing:

```python
print("Hello from Python")
```

Running `python3 hello.py` in Terminal produced the output:

```
Hello from Python
```

The message appeared successfully, confirming Python 3 is working correctly.

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| When translation / execution happens | Translates the entire source code into machine code **before** the program runs | Translates and executes the source code **line by line** at runtime |
| Typical output | Produces a standalone executable file (machine code) | Does not produce a separate file; executes directly from the source |
| One example | `gcc` (compiles C code into an executable binary) | `python3` (interprets Python scripts line by line) |
| One advantage | Faster execution after compilation since the code is already in machine language | Easier to test and debug because you can run code immediately without a compilation step |

**Explanation in my own words:**

A compiler reads the entire source code at once and translates it into machine code before the program runs. This creates a separate executable file that the computer can run directly, which makes execution fast. However, you need to recompile every time you make a change.

An interpreter, on the other hand, reads and executes the code one line at a time. There is no separate executable — the interpreter processes the source file each time you run it. This makes development quicker because you see results immediately after editing, but execution can be slower since translation happens every run.

Real programming languages sometimes combine both approaches. For instance, Python first compiles source code into bytecode (`.pyc` files) and then an interpreter (the Python virtual machine) executes that bytecode. This gives some benefits of both.

## 5. Difficulties faced

No major difficulties. The task was straightforward.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `hello.py` — the Python program.
- This README with the comparison table and explanation.

## 8. Commit details

- **Commit message:** "Compare compilers and interpreters"
- Pushed to GitHub and verified.
