import copy
import math

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


class BoardGraph(object):
    """The whole board, as a directed graph."""

    def __init__(self, board = ""):
        self.size = None
        self.tile_array = []
        self.edges = {}
        self.eat(board)

    def  __repr__(self):
        string = ""
        for col in self.tile_array:
            line = ' '.join([ str(t) for t in col])
            string += line + "\n"

        return string

    def eat(self, board):
        """Read board string and populate graph with Tile nodes and Edges."""

        self.size = int(math.sqrt(len(board)/2))
        
        # Build array:
        for i in range(self.size):
            col = []
            for j in range(self.size):
                tile_code, board = board[:2], board[2:]
                this_tile = Tile(i, j, tile_code)
                self.edges[(i,j)] = []
                col.append(this_tile)
            self.tile_array.append(col)

        # From Tile array, build Edge list:
        for i in range(self.size):
            for j in range(self.size):
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

    def path_to_closest(self, i, j, goals=["[]"]):
        """Find path to Tile closest to (i,j) that is of one of the types in "goals".
        This is a breadth-first search in a graph. Returns the
        path joining (i,j) with destination."""

        visited = []
        paths = [ [(i,j)] ]

        for i in range(self.size*self.size): # worst case, avoid infinite loops
            new_paths = []
            for path in paths:
                xy = path[-1]
                for edge in self.edges[xy]:
                    dest_xy = (edge.dest.pos_x, edge.dest.pos_y)
                    if not dest_xy in visited:
                        visited.append(dest_xy)
                        new_path = path + [ dest_xy ]
                        new_paths.append(new_path)
                        x, y = dest_xy
                        if self.tile_array[x][y].type in goals:
                            return path + [ dest_xy ]

            paths = new_paths

        return [ (i,j) ]


if __name__ == "__main__":
    board  = '##@1    ####    @4##'
    board += '      ########      '
    board += '        ####        '
    board += '    []        []    '
    board += '$-    ##    ##    $-'
    board += '$-    ##    ##    $-'
    board += '    []        []    '
    board += '        ####  @3    '
    board += '      ########      '
    board += '##@2    ####      ##'

    # Define map:
    M = BoardGraph()
    M.eat(board)
    print(M)

    # Find path:
    path = M.path_to_closest(3, 0, ["$-", "[]"])

    # Print out result in a second map:
    N = copy.deepcopy(M)
    print "----\n"
    for x,y in path[:-1]:
        N.tile_array[x][y] = Tile(x, y, "::")
    print(N)
