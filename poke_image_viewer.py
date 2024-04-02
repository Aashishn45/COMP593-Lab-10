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
import poke_api
import image_lib

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
    os.makedirs(images_dir)


# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.minsize(500, 600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("PokeImageViewer.COMP593")
root.iconbitmap(os.path.join(script_dir, "poke_ball.ico"))

# TODO: Create frames
frm = ttk.Frame(root)
frm.grid(sticky="nsew")
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)


# TODO: Populate frames with widgets and define event handler functions
image_pth = os.path.join(script_dir, "poke_ball.png")
photo = PhotoImage(file=image_pth)
img_label = ttk.Label(frm, image=photo)
img_label.grid(row=0, column=0, padx=10, pady=10)

poke_names = poke_api.get_pok_names()
if not poke_names:
    poke_names = []

pok_cmbox = ttk.Combobox(frm, values=poke_names, state="readonly")
pok_cmbox.set("Select a Pokemon")
pok_cmbox.grid(row=1, column=0, pady=10)

def select_pokemon(event):
    poke = pok_cmbox.get()
    image_path = poke_api.get_pok_art(poke, images_dir)
    if image_path:
        photo["file"] = image_path
        img_label["image"] = photo
        img_label["text"] = ""
    else:
        img_label["text"] = "No artwork available"
        img_label["image"] = None


pok_cmbox.bind("<<ComboboxSelected>>", select_pokemon)


desk_but = ttk.Button(frm, text="Set as Desktop Image", command=)
desk_but.grid(row=3, column=0)

root.mainloop()