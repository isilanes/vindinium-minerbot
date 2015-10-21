from libvindinium import Graph

class Game(object):
    """Take state JSON object and build a whole "game-status" object."""

    def __init__(self, state):
        self.state = state
        self.board = Graph.BoardGraph(state['game']['board']["tiles"])
        self.heroes = [ Hero(state['game']['heroes'][i]) for i in range(len(state['game']['heroes'])) ]
        self.me = Hero(state["hero"])
        # All ids but mine:
        self.other_ids = range(1,self.me.id) + range(self.me.id+1,5)

    def path_to_closest_mine(self):
        """Returns path to closest mine that is not my own."""

        i = self.me.pos["x"]
        j = self.me.pos["y"]
        opts = [ "$-" ]
        for id in self.other_ids:
            opts.append("${0}".format(id))

        return self.board.path_to_closest(i, j, opts)

    def get_dir_from_path(self, path):
        """Returns first direction to move to follow given path."""

        # len(path) >= 2 always (starting tile, plus destination one, plus all
        # in between, if any), except if we are already ON the destination tile.
        if len(path) == 1:
            return "Stay"
        else:
            dx = path[1][0] - path[0][0]
            if dx > 0:
                return "South"
            elif dx < 0:
                return "North"
            else:
                dy = path[1][1] - path[0][1]
                if dy > 0:
                    return "East"
                elif dy < 0:
                    return "West"
                else:
                    return "Stay" # we should never get here

    def which_dir_closest_mine(self):
        """Returns first move to follow path to closest mine that is not mine."""

        path = self.path_to_closest_mine()

        return self.get_dir_from_path(path)

    def path_to_closest_tavern(self):
        """Returns path to closest tavern."""

        i = self.me.pos["x"]
        j = self.me.pos["y"]
        opts = [ "[]" ]

        return self.board.path_to_closest(i, j, opts)

    def which_dir_closest_tavern(self):
        """Returns first move to follow path to closest tavern."""

        path = self.path_to_closest_tavern()

        return self.get_dir_from_path(path)


class Hero(object):
    """Info of a given Hero."""

    def __init__(self, hero):
        self.name = hero['name']
        self.pos = hero['pos']
        self.life = hero['life']
        self.gold = hero['gold']
        self.id = hero['id']

