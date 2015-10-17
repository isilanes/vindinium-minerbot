board = '##@1    ####    @4##      ########              ####            []        []    $-    ##    ##    $-$-    ##    ##    $-    []        []            ####  @3          ########      ##@2    ####      ##'

class Tile(object):
    """Any tile is a node in a graph."""

    def __init__(self, pos):
        self.pos = pos # (x,y) tuple
