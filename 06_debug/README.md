# Project 6: Debug Using `pdb` — Python's Interactive Debugger

This project teaches you how to find and fix bugs using **Python's built-in debugger, `pdb`**.

You'll learn how to:
- Insert breakpoints
- Step through code
- Inspect variables
- Catch subtle bugs using real tools

---

## The Problem

The following script is meant to **calculate the factorial of a number**, but it always returns `1`. You’ll use `pdb` to figure out what’s going wrong.

### Your Tasks

1. Run the script using the debugger:
   ```bash
   python -m pdb main.py
   ```
2. Step through the code using:
    - n: next line
    - s: step into function
    - l: list current lines
    - p: print variable
    - c: continue execution
    - exit: exit debug session
3. Fix the bug in the code and re-run it.