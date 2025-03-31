import tkinter as tk

def on_key(event):
    label.config(text=f"Key Pressed: {event.char}")

root = tk.Tk()
root.bind("<Key>", on_key)

label = tk.Label(root, text="Press a key")
label.pack()

root.mainloop()