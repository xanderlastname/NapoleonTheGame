#main python file
#in cmd paste "python main.py"

class Player:
    def __init__(self, health, points):
        self.health = health
        self.points = points

class Event:
    def __init__(self, name, health, *attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

def question(*options, prompt):
    print(prompt)
    print("Please choose an option:")
    for option in options:
        current = options.index(prompt) + 1
        print(f"{current}. {option}")
