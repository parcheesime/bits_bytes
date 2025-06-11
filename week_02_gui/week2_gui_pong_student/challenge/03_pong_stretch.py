# 🎯 Stretch Challenge: Improve your Pong game!
# - Add a score that updates every bounce
# - Add a restart button
# - Change ball speed or color as difficulty increases

# Start from your mini project and add new features here.
# Begin with this starter code has hints on how to add score
# Next, think about how you can add a restart button!

import tkinter as tk

# Hint: Create a variable called `score` and set it to 0 here


class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(290, 190, 310, 210, fill='white')
        self.x = 4
        self.y = -4

    def move(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= 600:
            self.x = -self.x
        if pos[1] <= 0:
            self.y = -self.y


class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(250, 350, 350, 360, fill='blue')
        self.x = 0
        self.canvas.bind_all("<Left>", self.move_left)
        self.canvas.bind_all("<Right>", self.move_right)

    def move_left(self, evt):
        self.x = -10  # You can change this number to adjust paddle speed

    def move_right(self, evt):
        self.x = 10   # You can change this number to adjust paddle speed

    def move(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 600:
            self.x = 0


window = tk.Tk()
window.title("Pong Game")

canvas = tk.Canvas(window, width=600, height=400, bg="black")
canvas.pack()

# Hint: Create a Label widget here to show the score, and use .Label and .pack()

ball = Ball(canvas)
paddle = Paddle(canvas)


def game_loop():
    # Hint: Add `global score` here so you can update the score inside this function

    ball.move()
    paddle.move()
    pos = canvas.coords(ball.id)
    paddle_pos = canvas.coords(paddle.id)

    # Hint: Inside this if-block, where the ball hits the paddle,
    # add code to increase the score and update the Label text, score = score + 1
    if pos[3] >= paddle_pos[1] and pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
        if pos[3] <= paddle_pos[3]:
            ball.y = -ball.y

    if pos[3] >= 400:
        canvas.create_text(300, 200, text="Game Over", fill="red", font=("Arial", 24))
        return

    window.after(20, game_loop)


game_loop()
window.mainloop()
