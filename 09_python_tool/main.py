from rich.console import Console
from rich.table import Table

def display_task_table():
    tasks = [
        {"id": 1, "task": "Prepare Python course", "status": "In Progress"},
        {"id": 2, "task": "Record video lessons", "status": "Pending"},
        {"id": 3, "task": "Review assignments", "status": "Done"}
    ]

    table = Table(title="My To-Do List")

    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Task", style="magenta")
    table.add_column("Status", style="green")

    for t in tasks:
        table.add_row(str(t["id"]), t["task"], t["status"])

    console = Console()
    console.print(table)

if __name__ == "__main__":
    display_task_table()