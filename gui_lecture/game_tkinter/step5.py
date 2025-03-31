import tkinter as tk
import random



def move_button():
    """Moves the button and updates the score when clicked."""
    global score
    score += 1  # Increase score
    score_label.config(text=f"Score: {score}")  # Update score label

    new_x = random.randint(10, 350)
    new_y = random.randint(10, 350)
    button.place(x=new_x, y=new_y)

def countdown():
    """Decreases the timer every second and stops the game when time runs out."""
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left}s")
        root.after(1000, countdown)  # Call countdown every second
    else:
        button.config(state="disabled")  # Disable button when time is up
        timer_label.config(text="Game Over!")


root = tk.Tk()
root.title("Catch the Button Game")
root.geometry("400x400")

score = 0  # Initialize score

# Score label
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()

button = tk.Button(root, text="Catch Me!", font=("Arial", 12), command=move_button)
button.place(x=150, y=150)


time_left = 30  # Game duration in seconds

# Timer label
timer_label = tk.Label(root, text=f"Time Left: {time_left}s", font=("Arial", 14))
timer_label.pack()


root.after(1000, countdown)  # Start countdown
root.mainloop()