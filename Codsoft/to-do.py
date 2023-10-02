import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", "Task added successfully!")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task_to_delete = tasks[selected_task_index]
        confirmation = messagebox.askyesno("Confirm Deletion", f"Do you want to delete the task:\n'{task_to_delete}'?")
        if confirmation:
            del tasks[selected_task_index]
            update_listbox()
            messagebox.showinfo("Task Deleted", "Task deleted successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

app = tk.Tk()
app.title("Colorful To-Do List App")
app.geometry("400x400")  # Set initial window size

# Define colors
bg_color = "#FFE4E1"  # Misty Rose
btn_color = "#FF69B4"  # Hot Pink
text_color = "#333333"  # Dark Gray

# Set background color
app.configure(bg=bg_color)

tasks = []

frame = tk.Frame(app, bg=bg_color)
frame.pack(pady=10)

task_label = tk.Label(frame, text="Enter a Task:", bg=bg_color, fg=text_color)
task_label.pack()

entry = tk.Entry(app, width=40)
entry.pack()

add_button = tk.Button(app, text="Add Task", width=40, command=add_task, bg=btn_color, fg=text_color)
add_button.pack()

delete_button = tk.Button(app, text="Delete Task", width=40, command=delete_task, bg=btn_color, fg=text_color)
delete_button.pack()

listbox = tk.Listbox(app, width=40, height=10, selectbackground="yellow")
listbox.pack()

scrollbar = tk.Scrollbar(app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

app.mainloop()
