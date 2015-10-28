import os
import pylab
import numpy
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
A = []
with open(fn) as f:
    for line in f:
        date, time, elo = line.split()
        X.append(int(elo))
        A.append(numpy.mean(X))

# Plot:
pylab.figure(figsize=(10,6), dpi=120)
pylab.plot(X, "bo--")
pylab.plot(A, "g-")
pylab.xlabel("# partida")
pylab.ylabel("Elo")
pylab.show()
