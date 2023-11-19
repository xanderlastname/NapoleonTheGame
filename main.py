#main python file
#in cmd paste "python main.py"

class Player:
    def __init__(self, health, points):
        self.health = health
        self.points = points


def question(*prompts, question):
    lenPrompt = len(prompts)
    print(question)
    for prompt in prompts:
        print(prompt)

question('Yes', 'No', 'maybe', question="Do you want to do this")