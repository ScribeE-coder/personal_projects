import tkinter as tk
import random

# Compliment list
compliments = [
    "You're doing your best and it shows.",
    "Billie Jean loves you just as you are.",
    "You have excellent cozy energy.",
    "You survived today—that's a win.",
    "Your presence is comforting, like pancakes.",
    "You are a beautiful human being.",
    "You are smart, you are loved, and you matter."
]

# Random compliment picker
def give_compliment():
    message = random.choice(compliments)

    # where the compliment text appears on screen
    compliment_label.config(text=message + "\u2764\uFE0F")

# Setup window
root = tk.Tk()
root.title("Compliment Bot")
root.geometry("320x240")
root.configure(bg="#fdf6e3")

# Face (text emoji for now)
face_label = tk.Label(root, text="(＾▽＾)", font=("Arial", 30), bg="#fdf6e3")
face_label.pack(pady=10)

# Compliment display
compliment_label = tk.Label(root, text="", wraplength=280, font=("Arial", 20), bg="#fdf6e3")

# pady = x units above and below the y-axis
compliment_label.pack(pady=10)

# Button
button = tk.Button(root, text="Gimme a Compliment", command=give_compliment)
button.pack(pady=10)

# Run it
root.mainloop()

