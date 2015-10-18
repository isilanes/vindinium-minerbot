import math

board = '##@1    ####    @4##      ########              ####            []        []    $-    ##    ##    $-$-    ##    ##    $-    []        []            ####  @3          ########      ##@2    ####      ##'

class Tile(object):
    """Any tile is a node in a graph."""

    def __init__(self, pos):
        self.pos = pos # (x,y) tuple


class Edge(object):
    """An Edge object connects two Tile objects."""

    def __init__(self):
        self.origin = None
        self.destiny = None


class MapGraph(object):
    """The whole map, as a directed graph."""

    def __init__(self):
        pass

    def eat(self, board):
        """Read board string and populate graph with Tile nodes and Edges."""

        size = int(math.sqrt(len(board)/2))
        
        i, j = 0, 0
        while board:
            print i,j
            this_tile, board = board[:2], board[2:]
            if this_tile == "  " or this_tile[0] == "@":
                # Passable terrain. We can get into them, and from them
                # into surrounding ones:
                pass
            elif this_tile  == "[]" or this_tile[0] == "$":
                # Taverns and mines can be "accessed", but not moved from
                # them to somewhere else:
                pass
            j += 1
            if j >= size:
                j = 0
                i += 1


M = MapGraph()
M.eat(board)
