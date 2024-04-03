import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x420")
window.title("Dice Roll")

dice = ["dice-six-faces-one.png", "dice-six-faces-two.png", "dice-six-faces-three.png", "dice-six-faces-four.png", "dice-six-faces-five.png",
        "dice-six-faces-six.png"]

# Function to resize image
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

# Function to roll the dice
def roll_dice():
    image1 = resize_image(random.choice(dice), 150, 150)
    image2 = resize_image(random.choice(dice), 150, 150)
    label1.configure(image=image1)
    label2.configure(image=image2)
    label1.image = image1
    label2.image = image2

# Resizing images
image1 = resize_image(random.choice(dice), 150, 150)
image2 = resize_image(random.choice(dice), 150, 150)

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.image = image1
label2.image = image2

label1.place(x=0, y=100)
label2.place(x=300, y=100)

roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

window.mainloop()
