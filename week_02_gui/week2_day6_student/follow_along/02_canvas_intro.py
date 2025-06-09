import tkinter as tk

window = tk.Tk()
window.title("Canvas Drawing")

canvas = tk.Canvas(window, width=500, height=300, bg="white")
canvas.pack()

# Draw a line and an oval
canvas.create_line(50, 50, 200, 50, fill="blue", width=3)
canvas.create_oval(100, 100, 200, 200, outline="green", width=2)

window.mainloop()
