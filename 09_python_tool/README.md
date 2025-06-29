# Project 10: Explore a Python Tool — Rich

The `rich` library is a powerful and popular Python tool that lets you create beautiful, styled terminal output, including:

- Syntax-highlighted code blocks
- Styled text (bold, color, etc.)
- Tables
- Progress bars

In this project, you’ll **research how to use the `rich` library** and write a Python script that prints a styled table of tasks from a list.

## Objectives

- Practice researching Python libraries using [https://pypi.org/project/rich](https://pypi.org/project/rich)
- Learn how to install and import a third-party library
- Explore how to create tables using `rich.table.Table`

## Task

1. Install the `rich` library:
   ```bash
   pip install rich
    ```
2. Read the docs and figure out how to:
    - Create a Table using rich.table.Table
    - Print the table using Console().print()
3. Complete the script so that it prints a to-do list as a styled table in the terminal.

## Sample Output
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ ID   ┃ Task                    ┃ Status      ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1    │ Prepare Python course   │ In Progress │
│ 2    │ Record video lessons    │ Pending     │
│ 3    │ Review assignments      │ Done        │
└──────┴─────────────────────────┴─────────────┘
