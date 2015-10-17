def winner(state):
    """Returs who won (or None if tie)."""

    heroes = state["game"]["heroes"]

    dsu = [ (h["gold"], h["name"]) for h in heroes ]
    dsu.sort()
    dsu.reverse()

    if dsu[0][0] == dsu[1][0]: # a tie, no one wins
        return None
    else:
        return dsu[0][1]
