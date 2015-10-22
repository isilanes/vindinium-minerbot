def winner(state):
    """Returns who won (or None if tie)."""

    try:
        heroes = state["game"]["heroes"]
    except:
        print("Can't find winner")
        return None

    dsu = [ (h["gold"], h["name"]) for h in heroes ]
    dsu.sort()
    dsu.reverse()

    if dsu[0][0] == dsu[1][0]: # a tie, no one wins
        return None
    else:
        return dsu[0][1]

def my_position(state):
    """Returns my position in the match."""

    pass
    

