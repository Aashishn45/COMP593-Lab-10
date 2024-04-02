"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
import ctypes
from tkinter import ttk, Tk, PhotoImage
import os

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
    os.makedirs(images_dir)


# Create the main window
root = Tk()
root.title("Pokemon Viewer")

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("PokeImageViewer.COMP593")
root.iconbitmap(os.path.join(script_dir, "poke_ball.ico"))

# TODO: Create frames
frm = ttk.Frame(root)
frm.grid(sticky="nsew")


# TODO: Populate frames with widgets and define event handler functions
image_pth = os.path.join(script_dir, "poke_ball.png")
photo = PhotoImage(file=image_pth)
img_label = ttk.Label(frm, image=photo)
img_label.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()