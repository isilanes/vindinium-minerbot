import datetime

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

def my_result(state, o):
    """Returns my position in the classification of the match."""

    dsu = []
    for h in state["game"]["heroes"]:
        try:
            dsu.append([h["gold"], h["name"], h["userId"]])
        except:
            dsu.append([h["gold"], h["name"], "--"])

    dsu.sort()
    dsu.reverse()

    for i, h in enumerate(dsu):
        if h[2] == o.user_id:
            return i + 1

def save_elo(state, o):
    """Saves my current elo rating with a time stamp."""

    elo = state["hero"]["elo"]
    now = datetime.datetime.now()

    string = "{0} {1}\n".format(now, elo)
    fn = "/home/isilanes/.vindinium/{0}.elo".format(o.user_id)

    with open(fn, "a") as f:
        f.write(string)
