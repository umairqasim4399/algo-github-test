import random
import json

def RandomCommands() -> (list):
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)

    return random_commands