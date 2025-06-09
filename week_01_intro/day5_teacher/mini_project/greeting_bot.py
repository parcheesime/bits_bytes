# Mini Project: Build a Greeting Bot 🤖

def ask_name():
    name = input("What's your name? ")
    return name

def ask_feeling():
    feeling = input("How are you feeling today? ")
    return feeling

def respond(name, feeling):
    print(f"Hi {name}! It's great to hear that you're feeling {feeling}. 😊")

# Let's put it all together!
user_name = ask_name()
user_feeling = ask_feeling()
respond(user_name, user_feeling)
