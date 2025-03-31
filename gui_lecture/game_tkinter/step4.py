import tkinter as tk
import random

root = tk.Tk()
root.title("Catch the Button Game")
root.geometry("400x400")

score = 0  # Initialize score

# Score label
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()


def move_button():
    """Moves the button and updates the score when clicked."""
    global score
    score += 1  # Increase score
    score_label.config(text=f"Score: {score}")  # Update score label

    new_x = random.randint(10, 350)
    new_y = random.randint(10, 350)
    button.place(x=new_x, y=new_y)


button = tk.Button(root, text="Catch Me!", font=("Arial", 12), command=move_button)
button.place(x=150, y=150)

root.mainloop()