import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.resizable(False, False)

# List to store tasks
tasks = []

# Function to update the listbox
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete selected task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to clear all tasks
def clear_all():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
    if confirm:
        tasks.clear()
        update_listbox()

# GUI Layout
title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=10)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=clear_all)
clear_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
