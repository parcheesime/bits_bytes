# 🟡 Week 2 – Smart Logic & Creative Loops

**Theme:** Decision-making, repetition, and drawing with code

Welcome to Week 2! This week we dive into the logic behind real programs — conditionals, loops, and lists — while building interactive programs and creative art with Turtle. Students will explore how computers make decisions and repeat actions, then apply those skills in their own mini projects.

Students continue using the learning structure: follow-along, fill-in-the-code, code puzzles, mini projects, open-ended challenges, and advanced teasers. Pair programming is encouraged!

---

## 🗓️ Day-by-Day Breakdown

### 📅 Day 1 – If/Else Decisions
**Mini Project:** Fortune Teller

#### 🔍 Follow-Along
```python
answer = input("Do you want to know your fortune? (yes/no): ")
if answer == "yes":
    print("You will have a lucky day!")
else:
    print("Maybe next time...")
```

#### ✍️ Fill in the Code
```python
# question = input("Do you like pizza? (yes/no): ")
# if question == "yes":
#     print("You're a legend!")
# else:
#     print("More for me then!")
```

#### 🧩 Code Puzzle
Rearrange these lines into a working program:
```python
# print("You chose pizza!")
# food = input("Do you want pizza or tacos? ")
# if food == "pizza":
# else:
#     print("You chose tacos!")
```

#### 🚀 Mini Project Prompt
Create a mini **Fortune Teller**:
- Ask 2–3 questions
- Give a fun, different fortune based on user input
- Use at least one `if/else` or `if/elif/else` block

#### 🎯 Challenge
Create a fortune teller with multiple paths:
- Ask for a number or color and use it to decide a random fortune
- Add at least 3 different possible outcomes

#### 📈 Advanced Teaser
- Use `.lower()` to clean input and avoid capitalization bugs
- Try nesting one `if` inside another
- Introduce `in` keyword: `if answer in ["yes", "y"]:`

---

### 📅 Day 2 – While Loops (Repeat Until)
**Mini Project:** Number Guesser
- Create a loop that runs until the player guesses the right number
- Add feedback ("too high" / "too low")
- Advanced Teaser: Track number of attempts, add "play again" logic

---

### 📅 Day 3 – For Loops + Lists
**Mini Project:** Mini Quiz Game
- Loop through a list of questions or fun facts
- Print score at the end
- Challenge: Allow multiple topics (list of lists)
- Advanced Teaser: Use dictionaries for structured questions/answers

---

### 📅 Day 4 – 🐢 Turtle + OOP Day: Art with Code
**Mini Project:** TurtleBot Art Generator
- Use `import turtle` to draw patterns
- Introduce classes: `class TurtleBot` with drawing methods
- Challenge: Students design their own shape/drawing bot
- Advanced Teaser: Add randomness, multiple turtles, or user input

---

### 📅 Day 5 – 🧠 Cumulative Mini Project: Inventory Collector or Quiz Builder
Students choose one:
1. **Inventory Collector** – pick up items in a text-based world (use lists, loops, if/else)
2. **Custom Quiz Builder** – build their own quiz and ask others to try it

#### 🎯 Extensions:
- Add difficulty levels
- Organize code into simple helper functions
- Use input sanitization (`.lower()`, `.strip()`)

---

Week 2 is where logic meets creativity — and students start building truly interactive, dynamic projects!
