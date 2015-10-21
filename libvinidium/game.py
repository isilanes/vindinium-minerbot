from libvinidium import graph

class Game(object):
    """Take state JSON object and build a whole "game-status" object."""

    def __init__(self, state):
        self.state = state
        self.board = graph.BoardGraph(state['game']['board'])
        self.heroes = [ Hero(state['game']['heroes'][i]) for i in range(len(state['game']['heroes'])) ]


class Hero(object):

    def __init__(self, hero):
        self.name = hero['name']
        self.pos = hero['pos']
        self.life = hero['life']
        self.gold = hero['gold']

