#!/usr/bin/env python

import fileinput
from visibility_graph import visibility_graph
import sys
from networkx import write_edgelist

# read time series from file given or from STDIN
series = []
for line in fileinput.input():
    series.append( float(line.strip()) )

# create graph
g = visibility_graph(series)

# print out edgelist
write_edgelist(g, sys.stdout, data=False)
