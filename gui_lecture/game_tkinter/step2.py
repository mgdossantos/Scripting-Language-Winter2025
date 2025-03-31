import tkinter as tk

root = tk.Tk()
root.title("Catch the Button Game")
root.geometry("400x400")

# Create the button
button = tk.Button(root, text="Catch Me!", font=("Arial", 12))
button.place(x=150, y=150)  # Initial position

root.mainloop()