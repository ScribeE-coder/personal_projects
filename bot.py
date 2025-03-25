import tkinter as tk
import random

# Compliment list
compliments = [
    "You're doing your best and it shows.",
    "Billie Jean loves you just as you are.",
    "You have excellent cozy energy.",
    "You survived today—that's a win.",
    "Your presence is comforting, like pancakes."
]

# Random compliment picker
def give_compliment():
    message = random.choice(compliments)
    compliment_label.config(text=message)

# Setup window
root = tk.Tk()
root.title("Compliment Bot")
root.geometry("320x240")
root.configure(bg="#fdf6e3")

# Face (text emoji for now)
face_label = tk.Label(root, text="(＾▽＾)", font=("Arial", 28), bg="#fdf6e3")
face_label.pack(pady=10)

# Compliment display
compliment_label = tk.Label(root, text="", wraplength=280, font=("Arial", 12), bg="#fdf6e3")
compliment_label.pack(pady=10)

# Button
button = tk.Button(root, text="Gimme a Compliment", command=give_compliment)
button.pack(pady=10)

# Run it
root.mainloop()

