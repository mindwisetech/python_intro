import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")

        self.tasks = []

        # Entry and add button
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack()

        # Frame for task list
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_labels = []

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Input error", "Task cannot be empty.")
            return

        label = tk.Label(self.frame, text=task_text, anchor="w", width=40, bg="white")
        label.bind("<Button-1>", lambda e, lbl=label: self.mark_done(lbl))
        label.pack(pady=2)

        self.task_labels.append(label)
        self.tasks.append(task_text)
        self.entry.delete(0, tk.END)

    def mark_done(self, label):
        label.config(bg="lightgreen", fg="gray", text="✔ " + label.cget("text"))

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()