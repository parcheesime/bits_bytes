import tkinter as tk

# TODO: Create the main window
window = tk.Tk()
# Set the window title
window.title("__________")  # ← Fill in the title

# TODO: Create a canvas widget (width=500, height=300, white background)
canvas = tk.Canvas(window, width=______, height=______, bg="__________")
canvas.pack()

# TODO: Draw a red horizontal line
canvas.create_line(______, ______, ______, ______, fill="__________", width=2)

# TODO: Draw a yellow rectangle with black outline
canvas.create_rectangle(______, ______, ______, ______, outline="__________", fill="__________")

# TODO: Run the app
window.__________()
