# Fill in the code to complete this button app.
import tkinter as tk

# TODO: Define the function to change the label text
def change_text():
    # Fill this in to update the label
    pass

# TODO: Create the window
window = tk.Tk()
# Set the window title
window.title("__________")  # ← fill in title
# Set the window size
window.geometry("__________")  # ← fill in geometry

# TODO: Add a label that starts with "Waiting..."
label = tk.Label(window, text="__________")  # ← fill in text
label.pack()

# TODO: Add a button that runs the function when clicked
button = tk.Button(window, text="__________", command=__________)  # ← fill in text and command
button.pack()

# TODO: Run the app
window.__________()  # ← what method goes here?
