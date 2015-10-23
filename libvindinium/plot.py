import os
import pylab
import argparse

#------------------------------------------------------------------------------#

# Read arguments:
parser = argparse.ArgumentParser()

parser.add_argument("--user-id",
        help="User ID. Default: 6ma0lt4d (isilanes).",
        default="6ma0lt4d")

o = parser.parse_args()

#------------------------------------------------------------------------------#

fn = os.path.join(os.environ["HOME"], '.vindinium', '{0}.elo'.format(o.user_id))

# Read data:
X = []
with open(fn) as f:
    for line in f:
        date, time, elo = line.split()
        X.append(elo)

# Plot:
pylab.figure(figsize=(10,6), dpi=120)
pylab.plot(X, "bo-")
pylab.xlabel("# partida")
pylab.ylabel("Elo")
pylab.show()
