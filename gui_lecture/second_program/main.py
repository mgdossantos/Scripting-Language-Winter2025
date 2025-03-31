import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter App")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

def greet():
    name = entry.get()
    greeting_label.config(text=f"Hello, {name}!")

button = tk.Button(root, text="Greet", command=greet)
button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

root.mainloop()