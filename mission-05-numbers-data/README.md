# Mission 5 — Numbers and data

## 1. Task / objective

Convert decimal, binary and hexadecimal values by hand, verify results with Python, build a small number converter program, and explain text encoding.

## 2. Work completed

Completed all manual conversions, verified them in the Python interactive shell, built and tested `number_converter.py`, and answered the text-encoding questions.

## 3. Commands / tools used

- `python3` (interactive mode) — used `bin()`, `int()`, `hex()` to verify conversions.
- `python3 number_converter.py` — ran the converter program.
- A text editor to create `number_converter.py`.

## 4. My understanding

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
|----------|------------------------|
| Convert decimal 13 to binary | 13 ÷ 2 = 6 R1, 6 ÷ 2 = 3 R0, 3 ÷ 2 = 1 R1, 1 ÷ 2 = 0 R1. Read remainders bottom-up → **1101** |
| Convert decimal 25 to binary | 25 ÷ 2 = 12 R1, 12 ÷ 2 = 6 R0, 6 ÷ 2 = 3 R0, 3 ÷ 2 = 1 R1, 1 ÷ 2 = 0 R1. → **11001** |
| Convert binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = 8 + 0 + 2 + 0 = **10** |
| Convert binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 8 + 4 + 0 + 1 = **13** |
| Convert hexadecimal A to decimal | A = **10** |
| Convert hexadecimal 1F to decimal | 1×16 + F×1 = 16 + 15 = **31** |
| Convert binary 1111 to hexadecimal | 1111 in decimal = 15, and 15 in hex = **F** |

### Task 5.2 — Verify using Python

I opened the Python interactive environment and checked each conversion:

- `bin(13)` → `'0b1101'` ✓ matches
- `bin(25)` → `'0b11001'` ✓ matches
- `int('1010', 2)` → `10` ✓ matches
- `int('1101', 2)` → `13` ✓ matches
- `int('A', 16)` → `10` ✓ matches
- `int('1F', 16)` → `31` ✓ matches
- `hex(int('1111', 2))` → `'0xf'` ✓ matches

All Python results matched my manual calculations.

### Task 5.3 — Build a small number converter

The `number_converter.py` program asks the user for a decimal number and displays both its binary and hexadecimal equivalents using Python's built-in `bin()` and `hex()` functions.

- `bin()` converts an integer to a binary string prefixed with `0b`.
- `hex()` converts an integer to a hexadecimal string prefixed with `0x`.

**Test results:**

| Test number | Binary output | Hexadecimal output |
|-------------|--------------|-------------------|
| 7 | 0b111 | 0x7 |
| 42 | 0b101010 | 0x2a |
| 255 | 0b11111111 | 0xff |

### Task 5.4 — How is text stored?

- **ASCII decimal code for uppercase A:** 65
- **ASCII decimal code for lowercase a:** 97
- **Why an encoding standard is needed:** Computers store everything as numbers. An encoding standard maps specific numbers to specific characters so that every computer agrees on what number means what letter. Without a standard, text created on one machine could display as gibberish on another.
- **Character not part of basic ASCII:** The emoji 😊 (or any character like ñ, ü, or ₹) is not in the basic 128-character ASCII set. These require a wider encoding like UTF-8.

## 5. Difficulties faced

No major difficulties. I briefly confused the direction of reading remainders during binary conversion (bottom-up, not top-down).

## 6. How I resolved them

I drew the division steps out carefully and remembered to read the remainders from the last division upwards.

## 7. Evidence / files

- `number_converter.py` — the working converter program.
- This README with manual working, Python verification and test results.

## 8. Commit details

- **Commit message:** "Build number converter and practise data representation"
- Pushed to GitHub and verified.
