import math

board = '##@1    ####    @4##      ########              ####            []        []    $-    ##    ##    $-$-    ##    ##    $-    []        []            ####  @3          ########      ##@2    ####      ##'

class Tile(object):
    """Any tile is a node in a graph."""

    def __init__(self, pos_x, pos_y, tile_type):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = tile_type

    def __repr__(self):
        return self.type


class Edge(object):
    """An Edge object connects two Tile objects."""

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __repr__(self):
        return '({0.pos_x}, {0.pos_y}) --> ({1.pos_x}, {1.pos_y})'.format(self.src, self.dest)


class MapGraph(object):
    """The whole map, as a directed graph."""

    def __init__(self):
        self.tile_array = []
        self.edges = {}

    def eat(self, board):
        """Read board string and populate graph with Tile nodes and Edges."""

        size = int(math.sqrt(len(board)/2))
        
        # Build array:
        for i in range(size):
            col = []
            for j in range(size):
                tile_code, board = board[:2], board[2:]
                this_tile = Tile(i, j, tile_code)
                self.edges[(i,j)] = []
                col.append(this_tile)
            self.tile_array.append(col)

        # From Tile array, build Edge list:
        for i in range(size):
            for j in range(size):
                this_tile = self.tile_array[i][j]
                if this_tile.type == "  " or this_tile.type[0] == "@":
                    # Only passable terrain and tiles with a hero (hence,
                    # passable), have outgoing edges:
                    for di,dj in [ (-1,0), (0,1), (1,0), (0,-1) ]: # up, right, down, left
                        if i + di < 0 or j + dj < 0:
                            continue
                        try:
                            other_tile = self.tile_array[i+di][j+dj]
                        except IndexError:
                            # other_tile is outside board
                            continue
                        if other_tile.type != "##": # only impassable tiles have no inbound Edges
                            E = Edge(this_tile, other_tile)
                            self.edges[(i,j)].append(E)

        for col in self.tile_array:
            print col


M = MapGraph()
M.eat(board)
