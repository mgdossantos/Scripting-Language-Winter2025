import tkinter as tk
import random

count = 0


def move_button():
    global count
    count += 1
    new_x = random.randint(20, 340)
    new_y = random.randint(20, 340)

    # button.place(x=new_x, y=new_y)


root = tk.Tk()
root.title("Catch the button Game")

root.geometry("400x400")
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16), fg="white", bg="blue")
label.pack(side="top", pady=10)  # Ensure it stays at the top

button = tk.Button(root, text="Click Me", font=("Arial", 17), wraplength=100, command=move_button)
button.place(x=150, y=150)

root.mainloop()
