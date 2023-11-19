#main python file
#in cmd paste "python main.py"

class Player:
    def __init__(self, health, points):
        self.health = health
        self.points = points


def question(*prompts, question):
    print(question)
    print("Please choose an option:")
    for prompt in prompts:
        current = prompts.index(prompt) + 1
        print(f"{current}. {prompt}")
