# Fill in the code to complete this button app.
import tkinter as tk


# TODO: Define the function to change the label text
def change_text():
    label.config(text="Hi there!", bg='red')
    pass


# TODO: Create the window
window = tk.Tk()
# Set the window title
window.title("Puzzle py file")  # ← fill in title
# Set the window size
window.geometry("300x300")  # ← fill in geometry

# TODO: Add a label that starts with "Waiting..."
label = tk.Label(window, text="Click the button")  # ← fill in text
label.pack()

# TODO: Add a button that runs the function when clicked
button = tk.Button(window, text="Click ME!", command=change_text)  # ← fill in text and command
button.pack()

# TODO: Run the app
window.mainloop()  # ← what method goes here?
