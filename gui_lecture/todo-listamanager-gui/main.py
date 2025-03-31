import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

root.mainloop()