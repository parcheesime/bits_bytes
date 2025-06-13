# Puzzle: Unscramble the code!

things = {
    "tickled": "a dinosaur",
    "found": "a golden banana",
    "befriended": "a marshmallow"
}

action = random.choice(actions)
print(f"{name} went to {place} and {action} {thing}!")
import random
thing = things[action]
name = random.choice(names)
places = ("the museum", "the jungle", "the moon")
names = ("Luna", "Max", "Zoe")
place = random.choice(places)
actions = ("found", "tickled", "befriended")
