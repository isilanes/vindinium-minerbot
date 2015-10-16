from random import choice

from game import Game

class Bot(object):
    pass

class RandomBot(Bot):

    def move(self, state):
        #game = Game(state) # unused for random
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)
