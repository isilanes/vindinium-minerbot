from random import choice

from libvindinium import Game

class Bot(object):

    def __init__(self):
        self.dirs = ['Stay', 'North', 'South', 'East', 'West']

class RandomBot(Bot):

    def move(self, state):
        return choice(self.dirs)

class MinerBot(Bot):

    def move(self, state):
        game = Game.Game(state) # unused for random
        return choice(self.dirs)
