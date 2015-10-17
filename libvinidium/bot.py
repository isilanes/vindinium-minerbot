from random import choice

from game import Game

class Bot(object):

    def __init__(self):
        self.dirs = ['Stay', 'North', 'South', 'East', 'West']

class RandomBot(Bot):

    def move(self, state):
        #game = Game(state) # unused for random
        return choice(self.dirs)
