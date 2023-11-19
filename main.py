import sys
from time import sleep

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

# this function is used for intro and info it just makes it look better, copied and pasted from internet lol 0.05 delay is good
def typewrite(*paragraph: str, delay) -> None:
    for sentence in paragraph:
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay)
        print()
        sleep(delay)

def question(*options, prompt):
    print(prompt)
    current = 0
    for option in options:
        current += 1
        print(f"{current}. {option}")

    choice = input(f"Please choose an option from 1-{current}")
    return choice

# main is used to order and call everything else, it is automatically called when the file is run
def main():
    # points go to -10 you lose, its an indication of the correctness of your decisionmaking
    player = Player(health=100, points=0)

if __name__ == '__main__':
    main()