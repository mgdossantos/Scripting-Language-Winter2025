import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    label.config(text=f"Selected: {filepath}")

root = tk.Tk()
button = tk.Button(root, text="Open File", command=open_file)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()