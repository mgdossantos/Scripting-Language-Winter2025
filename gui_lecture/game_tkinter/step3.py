import tkinter as tk
import random

root = tk.Tk()
root.title("Catch the Button Game")
root.geometry("400x400")

def add_Label():
    label.pack_forget()


def move_button():
    new_x = random.randint(10, 350)
    new_y = random.randint(10, 350)
    button.place(x=new_x, y=new_y)

button = tk.Button(root, text="Catch Me!", font=("Arial", 12), command=add_Label)
button.place(x=150, y=150)  # Initial position

label = tk.Label(root, text="Hi")
label.pack()
root.mainloop()