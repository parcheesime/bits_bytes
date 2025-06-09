# 🟡 Week 2 – Smart Logic & Creative Loops (with Tkinter)

**Theme:** This week builds on loops and logic by introducing interactive graphics, animations, and object-oriented design. You'll learn how to make windows, draw shapes, build mini games, and use classes to manage your code like a game designer.

---

## 📅 Day 1 – Windows, Widgets & Canvas

🎯 **Goals:**
- Learn how to use `tkinter.Tk()` to create windows
- Add widgets: `Label`, `Button`, `Entry`
- Use `Canvas` to draw shapes
- Complete button and canvas puzzles
- Choose a mini-project using either widgets or canvas

🧠 **Key Concepts:**
- `window.title()`, `window.geometry()`
- `.pack()` to place elements
- `command=` to trigger a function
- `Canvas.create_line()`, `Canvas.create_rectangle()`

📚 Based on *Python for Kids*, Chapter 12

---

## 📅 Day 2 – Canvas Animations & Interactions

🎯 **Goals:**
- Display images on a canvas
- Use `.move()` and `.after()` to animate shapes
- Make canvas objects react to input or events
- Store objects in variables for later updates

🧠 **Key Concepts:**
- `canvas.move(object, dx, dy)`
- Creating an object with a variable:
  ```python
  ball = canvas.create_oval(50, 50, 100, 100, fill="blue")
  ```
- Updating position with `after()`:
  ```python
  def move():
      canvas.move(ball, 5, 0)
      window.after(50, move)
  ```

💡 Practice procedural animation and object control using IDs

---

## 📅 Day 3 – Intro to Classes & Object-Oriented Programming

🎯 **Goals:**
- Understand what classes are and why they’re useful
- Create classes to represent real-world objects (like balls, players)
- Add attributes (like color, speed) and methods (like move, bounce)
- Inherit behavior using `super()`

🧠 **Key Concepts:**
- `class ClassName:`
- `__init__(self)` method to initialize attributes
- `self.attribute` and custom methods
- Inheritance:
  ```python
  class Parent:
      def __init__(self): self.role = "guardian"

  class Child(Parent):
      def __init__(self):
          super().__init__()
          self.role = "student"
  ```

📚 Based on *Python for Kids*, Chapter 8

---

## 📅 Day 4 – Build a Bounce Game / Pong Clone

🎯 **Goals:**
- Use `Canvas` + `Classes` to build a working bouncing ball game
- Add paddles, walls, and basic collision logic
- Animate with `after()` and `canvas.move()`
- Add player control using keys or mouse

🧠 **Key Concepts:**
- Game loop logic and screen refresh
- Object-oriented design for ball and paddle
- Collision detection using `canvas.coords()`

📚 Based on *Python for Kids*, Chapters 13–14

---

## 📅 Day 5 – 🎲 Project Day or Extensions

🎯 **Options:**
- Finalize and polish a personal project
- Add extra features (score, sound, new sprites)
- Combine canvas + widgets in one app
- Share and reflect on the week’s work

🛠️ **Challenge Ideas:**
- Emoji Mood App (with dictionary + canvas)
- Rainbow arcs with looped `create_arc`
- Drawing app with multiple shape buttons
- Keyboard-controlled canvas game

---

## 🧠 Weekly Learning Targets

- ✅ Master `tkinter` windows and canvas drawing
- ✅ Control program flow with loops and functions
- ✅ Build animations and reactive canvas elements
- ✅ Understand and apply object-oriented programming
- ✅ Launch a custom mini project or game from scratch!
