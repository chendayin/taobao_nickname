import json
import random
import numpy as np


def random_nick():
    with open('data/adjective.json') as f:
        adjective = json.loads(f.read())
    with open('data/noun.json') as f:
        noun = json.loads(f.read())
    return adjective[random.randrange(len(adjective) - 1)] + '的' + noun[random.randrange(len(noun) - 1)] + str(
        np.random.randint(10, 100))


if __name__ == '__main__':
    nick = random_nick()
    print(nick)
