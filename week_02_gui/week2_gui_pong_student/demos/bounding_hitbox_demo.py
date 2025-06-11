import tkinter as tk

root = tk.Tk()
root.title("Circle vs Box - Bounding Box Collision")
canvas = tk.Canvas(root, width=400, height=300, bg='black')
canvas.pack()

# Create a square and a circle
square = canvas.create_rectangle(250, 190, 330, 270, fill="green")
circle = canvas.create_oval(50, 120, 130, 200, fill="blue")


# Move the circle toward the square
def move_right():
    canvas.move(circle, 10, 0)
    check_collision()


def check_collision():
    pos1 = canvas.coords(square)  # box
    pos2 = canvas.coords(circle)  # circle bounding box

    if (pos1[2] >= pos2[0] and pos1[0] <= pos2[2] and
        pos1[3] >= pos2[1] and pos1[1] <= pos2[3]):
        print("⚠️ Bounding Box Collision!")
        canvas.itemconfig(square, fill="red")
        canvas.itemconfig(circle, fill="red")
    else:
        print("✅ No Collision (visually or bounding box)")
        canvas.itemconfig(square, fill="green")
        canvas.itemconfig(circle, fill="blue")


btn = tk.Button(root, text="Move Circle →", command=move_right)
btn.pack()

root.mainloop()
