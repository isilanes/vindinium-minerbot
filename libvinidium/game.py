from libvinidium import graph

TAVERN = 0
AIR = -1
WALL = -2

PLAYER1 = 1
PLAYER2 = 2
PLAYER3 = 3
PLAYER4 = 4

AIM = {'North': (-1, 0),
       'East': (0, 1),
       'South': (1, 0),
       'West': (0, -1)}

class HeroTile(object):

    def __init__(self, id):
        self.id = id


class MineTile(object):

    def __init__(self, heroId = None):
        self.heroId = heroId


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

